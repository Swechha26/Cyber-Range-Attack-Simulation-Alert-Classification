#!/usr/bin/env python3
import time
import requests
import docker
import logging
from prometheus_client import start_http_server, Counter, Gauge

# -------------------------------
# CONFIGURATION
# -------------------------------
CALDERA_URL = "http://caldera:8888"
CALDERA_USER = "admin"
CALDERA_PASS = "caldera_password"   # CHANGE THIS in real deployment

# Control-layer web server port for Prometheus metrics
METRICS_PORT = 8001

# Docker client
docker_client = docker.from_env()

# -------------------------------
# PROMETHEUS METRICS
# -------------------------------
challenges_started = Counter(
    "control_challenges_started_total",
    "Total number of challenges triggered by control layer"
)

last_difficulty_level = Gauge(
    "control_last_difficulty_level",
    "Numeric representation of last selected difficulty"
)

scaling_actions = Counter(
    "control_scaling_actions_total",
    "Number of container scaling actions performed"
)

# -------------------------------
# LOGGING
# -------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [CONTROL] %(levelname)s: %(message)s"
)

# -------------------------------
# CALDERA LOGIN
# -------------------------------
def caldera_login():
    """Authenticate and return a session."""
    s = requests.Session()
    r = s.post(
        f"{CALDERA_URL}/login",
        json={"username": CALDERA_USER, "password": CALDERA_PASS}
    )

    if r.status_code != 200:
        logging.error("Caldera login failed: %s", r.text)
        return None

    logging.info("Logged in to Caldera successfully.")
    return s


# -------------------------------
# TRIGGER CALDERA OPERATION
# -------------------------------
def trigger_caldera_operation(adversary_id="disturb", name="auto-op"):
    """
    Trigger a Caldera operation using adversary profile.
    """
    s = caldera_login()
    if not s:
        return False

    payload = {
        "name": name,
        "adversary_id": adversary_id,
        "state": "running"
    }

    r = s.post(f"{CALDERA_URL}/api/v2/operations", json=payload)

    if r.status_code == 200 or r.status_code == 201:
        logging.info("Operation triggered: %s", r.text)
        challenges_started.inc()
        return True
    else:
        logging.error("Failed to trigger operation: %s", r.text)
        return False


# -------------------------------
# SCALE DOCKER CONTAINERS
# -------------------------------
def scale_service(service_name, replicas):
    """Scale a Docker Compose service via Docker SDK."""
    try:
        service = docker_client.services.get(service_name)
        service.scale(replicas)
        scaling_actions.inc()
        logging.info("Scaled %s to %d replicas", service_name, replicas)
        return True
    except Exception as e:
        logging.error("Scaling failed: %s", e)
        return False


# -------------------------------
# SIMPLE DIFFICULTY ENGINE
# (placeholder – link to RL model later)
# -------------------------------
def compute_difficulty(user_score=0.5):
    """
    Placeholder difficulty logic.
    0.0 = easy, 1.0 = hard.
    Example: increase difficulty for high-performing trainees.
    """
    if user_score > 0.7:
        level = 2  # hard
    elif user_score > 0.4:
        level = 1  # medium
    else:
        level = 0  # easy

    last_difficulty_level.set(level)
    return level


# -------------------------------
# MAIN LOOP
# -------------------------------
def main():
    logging.info("Starting Control Layer...")
    
    # Start Prometheus metrics endpoint
    start_http_server(METRICS_PORT)
    logging.info(f"Prometheus metrics exposed on :{METRICS_PORT}")

    while True:
        # Example dynamic difficulty (replace with real values later)
        user_score = 0.5
        difficulty = compute_difficulty(user_score)

        # Map difficulty to # of attackers
        attacker_count = {0: 1, 1: 2, 2: 3}.get(difficulty, 1)

        logging.info("Difficulty: %d | Attackers: %d", difficulty, attacker_count)

        # Trigger Caldera adversary operation
        trigger_caldera_operation()

        # Scale DVWA attackers (simulate multiple attack nodes)
        # NOTE: Works only if you're using Docker Swarm mode.
        # For Compose, we use CLI scaling instead.
        try:
            import subprocess
            subprocess.run(
                ["docker", "compose", "up", "--scale", f"dvwa={attacker_count}", "-d"]
            )
            scaling_actions.inc()
        except Exception as e:
            logging.error("Compose scaling failed: %s", e)

        logging.info("Sleeping before next cycle...")
        time.sleep(60)  # one cycle per minute


if __name__ == "__main__":
    main()
