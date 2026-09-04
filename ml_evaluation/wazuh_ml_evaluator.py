#!/usr/bin/env python3
"""
ML-assisted evaluation layer for the cyber range.

Pipeline:
Wazuh/Kibana logs -> feature extraction -> scenario classification ->
defender usefulness scoring -> automated report and difficulty recommendation.

The implementation intentionally uses only Python standard-library modules so it
can run in the lab without installing additional packages.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import re
import statistics
import ssl
import base64
import random
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib import request


SCENARIO_TO_MITRE = {
    "file_integrity": {
        "name": "File Integrity Change",
        "techniques": "T1565.001",
        "nice_roles": "Cyber Defense Analyst",
    },
    "command_execution": {
        "name": "Command Execution / Discovery",
        "techniques": "T1082, T1057",
        "nice_roles": "Cyber Defense Analyst",
    },
    "privilege_activity": {
        "name": "Privilege / Authentication Activity",
        "techniques": "T1548.003, T1078",
        "nice_roles": "Incident Responder / Cyber Defense Analyst",
    },
    "payload_drop": {
        "name": "Payload Delivery / File Drop",
        "techniques": "T1105",
        "nice_roles": "Cyber Defense Analyst",
    },
    "persistence_change": {
        "name": "Persistence / Config Change",
        "techniques": "T1053.003",
        "nice_roles": "Security Analyst / Incident Responder",
    },
    "container_noise": {
        "name": "Container Noise / Rootcheck Dominated",
        "techniques": "N/A",
        "nice_roles": "Cyber Defense Analyst / SOC Evaluation",
    },
}


TOKEN_RE = re.compile(r"[A-Za-z0-9_./:-]+")


def nested_get(data: dict[str, Any], dotted_key: str, default: Any = "") -> Any:
    current: Any = data
    for part in dotted_key.split("."):
        if not isinstance(current, dict) or part not in current:
            return default
        current = current[part]
    return current


def as_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, (list, tuple, set)):
        return " ".join(as_text(item) for item in value)
    if isinstance(value, dict):
        return " ".join(f"{key}:{as_text(val)}" for key, val in value.items())
    return str(value)


def tokenize(text: str) -> list[str]:
    return [token.lower() for token in TOKEN_RE.findall(text) if token.strip()]


def load_records(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        raise FileNotFoundError(path)

    if path.suffix.lower() == ".csv":
        with path.open(newline="", encoding="utf-8") as handle:
            return [normalize_record(dict(row)) for row in csv.DictReader(handle)]

    content = path.read_text(encoding="utf-8").strip()
    if not content:
        return []

    if path.suffix.lower() == ".json":
        parsed = json.loads(content)
        if isinstance(parsed, list):
            return [normalize_record(record) for record in parsed]
        if isinstance(parsed, dict):
            hits = nested_get(parsed, "hits.hits")
            if isinstance(hits, list):
                return [normalize_record(hit.get("_source", hit)) for hit in hits]
            return [normalize_record(parsed)]

    records = []
    for line in content.splitlines():
        line = line.strip()
        if not line:
            continue
        parsed = json.loads(line)
        records.append(normalize_record(parsed.get("_source", parsed)))
    return records


def normalize_record(record: dict[str, Any]) -> dict[str, Any]:
    """
    Filebeat may store the real Wazuh alert as a JSON string in `message`.
    For ML, prefer that inner alert because it contains the true Wazuh agent,
    rule, syscheck, decoder, and full_log fields.
    """
    message = record.get("message")
    if not isinstance(message, str) or not message.strip().startswith("{"):
        return record

    try:
        inner = json.loads(message)
    except json.JSONDecodeError:
        return record

    if not isinstance(inner, dict):
        return record

    normalized = dict(inner)
    normalized.setdefault("@timestamp", record.get("@timestamp", inner.get("timestamp")))
    normalized.setdefault("filebeat_agent", record.get("agent", {}))
    normalized.setdefault("filebeat_index", record.get("_index", ""))
    return normalized


def export_from_elasticsearch(
    url: str,
    index: str,
    output_path: Path,
    query: str | None,
    minutes: int,
    size: int,
    username: str | None = None,
    password: str | None = None,
    insecure: bool = False,
) -> None:
    must: list[dict[str, Any]] = [
        {"range": {"@timestamp": {"gte": f"now-{minutes}m", "lte": "now"}}}
    ]
    if query:
        must.append({"query_string": {"query": query}})

    payload = {
        "size": size,
        "sort": [{"@timestamp": {"order": "desc"}}],
        "query": {"bool": {"must": must}},
    }
    body = json.dumps(payload).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    if username and password:
        token = base64.b64encode(f"{username}:{password}".encode("utf-8")).decode("ascii")
        headers["Authorization"] = f"Basic {token}"

    req = request.Request(
        f"{url.rstrip('/')}/{index}/_search",
        data=body,
        headers=headers,
        method="POST",
    )

    context = ssl._create_unverified_context() if insecure else None
    with request.urlopen(req, timeout=20, context=context) as response:
        parsed = json.loads(response.read().decode("utf-8"))

    hits = parsed.get("hits", {}).get("hits", [])
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as handle:
        for hit in hits:
            handle.write(json.dumps(hit.get("_source", hit), sort_keys=True) + "\n")


def scenario_label(record: dict[str, Any]) -> str:
    explicit = record.get("scenario") or record.get("scenario_label") or record.get("label")
    if explicit:
        return str(explicit)

    text = feature_text(record).lower()
    agent_id = str(nested_get(record, "agent.id", record.get("agent_id", "")))

    if agent_id == "002" and "rootcheck" in text:
        return "container_noise"
    if "/etc/hosts" in text or "syscheck" in text and "hosts" in text:
        return "file_integrity"
    if "payload_test.sh" in text or "/etc/profile.d" in text:
        return "payload_drop"
    if "/etc/crontab" in text or "cron" in text:
        return "persistence_change"
    if "sudo" in text or "pam:" in text or "session opened" in text:
        return "privilege_activity"
    if "execve" in text or "ausearch" in text or "whoami" in text or "uname" in text or "ps aux" in text:
        return "command_execution"
    if agent_id == "002":
        return "container_noise"
    return "unknown"


def feature_text(record: dict[str, Any]) -> str:
    fields = [
        "@timestamp",
        "agent.id",
        "agent.name",
        "rule.id",
        "rule.level",
        "rule.description",
        "rule.groups",
        "rule.mitre.id",
        "decoder.name",
        "location",
        "full_log",
        "syscheck.path",
        "syscheck.event",
        "syscheck.sha256_after",
        "syscheck.sha256_before",
        "data.audit.exe",
        "data.audit.command",
        "data.srcuser",
        "data.dstuser",
    ]
    parts = []
    for field in fields:
        value = nested_get(record, field, record.get(field, ""))
        if value != "":
            parts.append(f"{field}={as_text(value)}")
    return " ".join(parts)


def usefulness_score(record: dict[str, Any], predicted_scenario: str) -> tuple[int, str]:
    text = feature_text(record).lower()
    if predicted_scenario == "container_noise" or "rootcheck" in text:
        score = 10 if predicted_scenario == "container_noise" else 20
        return score, "Noise" if score < 15 else "Low"

    score = 0

    if "syscheck" in text:
        score += 35
    if "/etc/hosts" in text or "/etc/crontab" in text:
        score += 35
    if "sudo" in text or "pam" in text or "/var/log/auth.log" in text:
        score += 45
    if "/var/log/audit/audit.log" in text or "execve" in text or "audit" in text:
        score += 35
    if "payload_test.sh" in text or "/etc/profile.d" in text:
        score += 40
    if predicted_scenario == "privilege_activity":
        score += 25
    if predicted_scenario == "unknown":
        score -= 10

    score = max(0, min(100, score))
    if score >= 70:
        label = "High"
    elif score >= 40:
        label = "Medium"
    elif score >= 15:
        label = "Low"
    else:
        label = "Noise"
    return score, label


class NaiveBayesTextClassifier:
    def __init__(self) -> None:
        self.class_counts: Counter[str] = Counter()
        self.token_counts: dict[str, Counter[str]] = defaultdict(Counter)
        self.total_tokens: Counter[str] = Counter()
        self.vocabulary: set[str] = set()

    def fit(self, texts: list[str], labels: list[str]) -> None:
        for text, label in zip(texts, labels):
            self.class_counts[label] += 1
            tokens = tokenize(text)
            self.vocabulary.update(tokens)
            self.token_counts[label].update(tokens)
            self.total_tokens[label] += len(tokens)

    def predict_one(self, text: str) -> tuple[str, float]:
        if not self.class_counts:
            return "unknown", 0.0

        tokens = tokenize(text)
        vocab_size = max(1, len(self.vocabulary))
        total_docs = sum(self.class_counts.values())
        scores: dict[str, float] = {}

        for label, class_count in self.class_counts.items():
            log_prob = math.log(class_count / total_docs)
            denom = self.total_tokens[label] + vocab_size
            for token in tokens:
                token_count = self.token_counts[label][token]
                log_prob += math.log((token_count + 1) / denom)
            scores[label] = log_prob

        best_label = max(scores, key=scores.get)
        max_score = scores[best_label]
        probs = {label: math.exp(score - max_score) for label, score in scores.items()}
        confidence = probs[best_label] / sum(probs.values())
        return best_label, confidence

    def to_json(self) -> dict[str, Any]:
        return {
            "class_counts": dict(self.class_counts),
            "token_counts": {label: dict(counts) for label, counts in self.token_counts.items()},
            "total_tokens": dict(self.total_tokens),
            "vocabulary": sorted(self.vocabulary),
        }

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "NaiveBayesTextClassifier":
        model = cls()
        model.class_counts = Counter(data.get("class_counts", {}))
        model.token_counts = defaultdict(Counter)
        for label, counts in data.get("token_counts", {}).items():
            model.token_counts[label] = Counter(counts)
        model.total_tokens = Counter(data.get("total_tokens", {}))
        model.vocabulary = set(data.get("vocabulary", []))
        return model


def train_model(records: list[dict[str, Any]]) -> NaiveBayesTextClassifier:
    usable = [(feature_text(record), scenario_label(record)) for record in records]
    usable = [(text, label) for text, label in usable if label != "unknown"]
    if not usable:
        raise ValueError("No labelled or weak-labelled records were found.")

    model = NaiveBayesTextClassifier()
    model.fit([item[0] for item in usable], [item[1] for item in usable])
    return model


def evaluate_training(records: list[dict[str, Any]], model: NaiveBayesTextClassifier) -> dict[str, Any]:
    labels = [scenario_label(record) for record in records]
    predictions = [model.predict_one(feature_text(record))[0] for record in records]
    known = [(actual, pred) for actual, pred in zip(labels, predictions) if actual != "unknown"]
    correct = sum(1 for actual, pred in known if actual == pred)
    accuracy = correct / len(known) if known else 0.0
    confusion: dict[str, Counter[str]] = defaultdict(Counter)
    for actual, pred in known:
        confusion[actual][pred] += 1
    return {
        "records": len(records),
        "known_records": len(known),
        "accuracy": accuracy,
        "confusion": {label: dict(counts) for label, counts in confusion.items()},
    }


def load_model(path: Path) -> NaiveBayesTextClassifier:
    return NaiveBayesTextClassifier.from_json(json.loads(path.read_text(encoding="utf-8")))


def save_model(model: NaiveBayesTextClassifier, path: Path, metrics: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "type": "standard_library_multinomial_naive_bayes",
        "metrics": metrics,
        "model": model.to_json(),
    }
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def label_record_for_dataset(record: dict[str, Any]) -> str | None:
    text = feature_text(record).lower()
    agent_id = as_text(nested_get(record, "agent.id", record.get("agent_id", "")))
    agent_name = as_text(nested_get(record, "agent.name", "")).lower()

    if "payload_test.sh" in text or "/etc/profile.d" in text:
        return "payload_drop"
    if "/etc/crontab" in text or "cron" in text:
        return "persistence_change"
    if "sudo" in text or "pam:" in text or "/var/log/auth.log" in text or "session opened" in text:
        return "privilege_activity"
    if "execve" in text or "whoami" in text or "uname" in text or "key=exec" in text:
        return "command_execution"
    if "/etc/hosts" in text or ("syscheck" in text and "integrity checksum changed" in text):
        return "file_integrity"
    if agent_id == "002" or "target-linux" in agent_name or "rootcheck" in text:
        return "container_noise"
    return None


def cmd_build_dataset(args: argparse.Namespace) -> None:
    records = load_records(Path(args.input))
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    handles: dict[str, Any] = {}
    counts: Counter[str] = Counter()
    try:
        for record in records:
            label = label_record_for_dataset(record)
            if not label:
                continue
            record["scenario"] = label
            if label not in handles:
                handles[label] = (output_dir / f"{label}.jsonl").open("w", encoding="utf-8")
            handles[label].write(json.dumps(record, sort_keys=True) + "\n")
            counts[label] += 1
    finally:
        for handle in handles.values():
            handle.close()

    print(f"Dataset written to: {output_dir}")
    for label, count in counts.most_common():
        print(f"{label}: {count}")


def recommend_difficulty(records: list[dict[str, Any]], avg_usefulness: float, confidence: float) -> str:
    agent_counts = Counter(as_text(nested_get(record, "agent.id", record.get("agent_id", ""))) for record in records)
    container_ratio = agent_counts.get("002", 0) / max(1, len(records))

    if avg_usefulness >= 70 and confidence >= 0.75 and container_ratio < 0.5:
        return "Hard: increase stealth, add multi-step persistence, or require correlation across audit/auth/syscheck."
    if avg_usefulness >= 40:
        return "Medium: continue with similar ATT&CK technique and add one extra investigation step."
    return "Easy: repeat the scenario on VM target with clearer monitored paths before increasing complexity."


def build_report(records: list[dict[str, Any]], model: NaiveBayesTextClassifier) -> str:
    rows = []
    scenario_counts: Counter[str] = Counter()
    usefulness_counts: Counter[str] = Counter()
    agent_counts: Counter[str] = Counter()
    scores: list[int] = []
    confidences: list[float] = []

    for record in records:
        scenario, confidence = model.predict_one(feature_text(record))
        score, score_label = usefulness_score(record, scenario)
        scenario_counts[scenario] += 1
        usefulness_counts[score_label] += 1
        scores.append(score)
        confidences.append(confidence)
        agent_id = as_text(nested_get(record, "agent.id", record.get("agent_id", ""))) or "unknown"
        agent_counts[agent_id] += 1
        rows.append(
            {
                "timestamp": as_text(nested_get(record, "@timestamp", record.get("timestamp", ""))),
                "agent": agent_id,
                "scenario": scenario,
                "confidence": confidence,
                "usefulness": score_label,
                "score": score,
                "rule": as_text(nested_get(record, "rule.id", record.get("rule_id", ""))),
                "location": as_text(record.get("location", nested_get(record, "data.location", ""))),
            }
        )

    avg_usefulness = statistics.mean(scores) if scores else 0.0
    avg_confidence = statistics.mean(confidences) if confidences else 0.0
    recommendation = recommend_difficulty(records, avg_usefulness, avg_confidence)

    lines = [
        "# Cyber Range ML Evaluation Report",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        "",
        "## Summary",
        "",
        f"- Total records analyzed: {len(records)}",
        f"- Average model confidence: {avg_confidence:.2f}",
        f"- Average defender usefulness score: {avg_usefulness:.1f}/100",
        f"- Difficulty recommendation: {recommendation}",
        "",
        "## Scenario Distribution",
        "",
        "| Predicted Scenario | Count | MITRE Technique | NICE Role Relevance |",
        "| --- | ---: | --- | --- |",
    ]

    for scenario, count in scenario_counts.most_common():
        mapping = SCENARIO_TO_MITRE.get(scenario, {})
        lines.append(
            f"| {mapping.get('name', scenario)} | {count} | "
            f"{mapping.get('techniques', 'N/A')} | {mapping.get('nice_roles', 'N/A')} |"
        )

    lines.extend(
        [
            "",
            "## Defender Usefulness",
            "",
            "| Usefulness Level | Count |",
            "| --- | ---: |",
        ]
    )
    for label in ["High", "Medium", "Low", "Noise"]:
        lines.append(f"| {label} | {usefulness_counts.get(label, 0)} |")

    lines.extend(
        [
            "",
            "## Target Comparison",
            "",
            "| Agent ID | Records | Interpretation |",
            "| --- | ---: | --- |",
        ]
    )
    for agent, count in agent_counts.most_common():
        if agent == "004":
            interpretation = "VM target: expected richer audit/auth/syscheck telemetry"
        elif agent == "002":
            interpretation = "Container target: expected more limited or rootcheck-dominated telemetry"
        else:
            interpretation = "Unmapped target"
        lines.append(f"| {agent} | {count} | {interpretation} |")

    lines.extend(
        [
            "",
            "## Event-Level Predictions",
            "",
            "| Time | Agent | Scenario | Confidence | Usefulness | Score | Rule | Location |",
            "| --- | --- | --- | ---: | --- | ---: | --- | --- |",
        ]
    )
    for row in rows[:50]:
        scenario_name = SCENARIO_TO_MITRE.get(row["scenario"], {}).get("name", row["scenario"])
        lines.append(
            f"| {row['timestamp']} | {row['agent']} | {scenario_name} | "
            f"{row['confidence']:.2f} | {row['usefulness']} | {row['score']} | "
            f"{row['rule']} | {row['location']} |"
        )

    if len(rows) > 50:
        lines.append(f"| ... | ... | {len(rows) - 50} more events omitted | ... | ... | ... | ... | ... |")

    return "\n".join(lines) + "\n"


def cmd_train(args: argparse.Namespace) -> None:
    records = load_records(Path(args.input))
    model = train_model(records)
    metrics = evaluate_training(records, model)
    save_model(model, Path(args.model), metrics)
    print(f"Model saved: {args.model}")
    print(f"Records: {metrics['records']} | Known labels: {metrics['known_records']} | Training accuracy: {metrics['accuracy']:.2f}")


def cmd_report(args: argparse.Namespace) -> None:
    records = load_records(Path(args.input))
    model_payload = json.loads(Path(args.model).read_text(encoding="utf-8"))
    model = NaiveBayesTextClassifier.from_json(model_payload["model"])
    report = build_report(records, model)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report, encoding="utf-8")
    print(f"Report saved: {output}")


def cmd_export_es(args: argparse.Namespace) -> None:
    export_from_elasticsearch(
        url=args.url,
        index=args.index,
        output_path=Path(args.output),
        query=args.query,
        minutes=args.minutes,
        size=args.size,
        username=args.username,
        password=args.password,
        insecure=args.insecure,
    )
    print(f"Export saved: {args.output}")


def cmd_train_dir(args: argparse.Namespace) -> None:
    data_dir = Path(args.input_dir)
    records: list[dict[str, Any]] = []
    for path in sorted(data_dir.glob("*.jsonl")):
        label = path.stem
        if label == "all_filebeat" or label.startswith("all_"):
            continue
        for record in load_records(path):
            record["scenario"] = label
            records.append(record)

    if not records:
        raise ValueError(f"No scenario JSONL files found in {data_dir}")

    if args.max_per_class:
        by_label: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for record in records:
            by_label[scenario_label(record)].append(record)
        rng = random.Random(args.seed)
        balanced_records: list[dict[str, Any]] = []
        for label, label_records in by_label.items():
            rng.shuffle(label_records)
            balanced_records.extend(label_records[: args.max_per_class])
        records = balanced_records

    model = train_model(records)
    metrics = evaluate_training(records, model)
    save_model(model, Path(args.model), metrics)
    report = build_report(records, model)
    output = Path(args.report)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report, encoding="utf-8")
    print(f"Model saved: {args.model}")
    print(f"Report saved: {args.report}")
    print(f"Records: {metrics['records']} | Known labels: {metrics['known_records']} | Training accuracy: {metrics['accuracy']:.2f}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Cyber range Wazuh log ML evaluator")
    subparsers = parser.add_subparsers(required=True)

    train = subparsers.add_parser("train", help="Train scenario classifier from labelled or weak-labelled alerts")
    train.add_argument("--input", required=True, help="Input CSV, JSON, or JSONL Wazuh alerts")
    train.add_argument("--model", default="ml_evaluation/model.json", help="Output model path")
    train.set_defaults(func=cmd_train)

    train_dir = subparsers.add_parser("train-dir", help="Train from a directory of scenario-labelled JSONL files")
    train_dir.add_argument("--input-dir", required=True, help="Directory containing scenario JSONL files")
    train_dir.add_argument("--model", default="ml_evaluation/model.json", help="Output model path")
    train_dir.add_argument("--report", default="ml_evaluation/reports/training_report.md", help="Training report output path")
    train_dir.add_argument("--max-per-class", type=int, default=None, help="Limit records per class for balanced training")
    train_dir.add_argument("--seed", type=int, default=42, help="Random seed used with --max-per-class")
    train_dir.set_defaults(func=cmd_train_dir)

    report = subparsers.add_parser("report", help="Generate automated evaluation report")
    report.add_argument("--input", required=True, help="Input CSV, JSON, or JSONL Wazuh alerts")
    report.add_argument("--model", default="ml_evaluation/model.json", help="Trained model path")
    report.add_argument("--output", default="ml_evaluation/reports/latest_report.md", help="Report output path")
    report.set_defaults(func=cmd_report)

    build_dataset = subparsers.add_parser("build-dataset", help="Create scenario-labelled files from a mixed Wazuh/Filebeat export")
    build_dataset.add_argument("--input", required=True, help="Mixed JSONL export, for example all_filebeat.jsonl")
    build_dataset.add_argument("--output-dir", default="ml_evaluation/data/labelled", help="Output directory for labelled JSONL files")
    build_dataset.set_defaults(func=cmd_build_dataset)

    export_es = subparsers.add_parser("export-es", help="Export recent alerts from Elasticsearch")
    export_es.add_argument("--url", default="http://localhost:9200", help="Elasticsearch URL")
    export_es.add_argument("--index", default="wazuh-alerts-*", help="Elasticsearch index pattern")
    export_es.add_argument("--output", default="ml_evaluation/data/elasticsearch_export.jsonl", help="JSONL output path")
    export_es.add_argument("--query", default=None, help="Optional Kibana query_string query")
    export_es.add_argument("--minutes", type=int, default=60, help="Lookback window in minutes")
    export_es.add_argument("--size", type=int, default=500, help="Maximum records to export")
    export_es.add_argument("--username", default=None, help="Optional Elasticsearch username")
    export_es.add_argument("--password", default=None, help="Optional Elasticsearch password")
    export_es.add_argument("--insecure", action="store_true", help="Disable TLS certificate verification for local lab HTTPS")
    export_es.set_defaults(func=cmd_export_es)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
