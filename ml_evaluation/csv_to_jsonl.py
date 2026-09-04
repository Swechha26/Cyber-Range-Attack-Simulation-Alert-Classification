import pandas as pd
import json
import random

df = pd.read_csv("data/Data.csv")

with open("data/test.jsonl", "w") as f:
    for _, row in df.iterrows():

        text = str(row.iloc[0])

        # ✅ CLEAN TEXT
        text = text.lower().replace(",", " ").replace(";", " ")

        if not text.strip():
            continue

        # ✅ ADD SCENARIO DIVERSITY (VERY IMPORTANT)
        rand = random.random()

        if rand < 0.2:
            scenario = "privilege_activity"
            text += " sudo login authentication success"
            extra = {
                "data": {"srcuser": "root", "dstuser": "root"}
            }

        elif rand < 0.4:
            scenario = "persistence_change"
            text += " cron job scheduled"
            extra = {
                "syscheck": {"path": "/etc/crontab"}
            }

        elif rand < 0.6:
            scenario = "file_integrity"
            text += " file integrity changed hosts"
            extra = {
                "syscheck": {"path": "/etc/hosts"}
            }

        elif rand < 0.8:
            scenario = "payload_drop"
            text += " payload file dropped"
            extra = {
                "data": {"audit": {"command": "payload_test.sh"}}
            }

        else:
            scenario = "command_execution"
            text += " command executed uname whoami ps aux"
            extra = {
                "data": {"audit": {"command": text}}
            }

        # ✅ BUILD FULL STRUCTURED RECORD
        record = {
            "@timestamp": "2026-01-01T00:00:00Z",
            "agent": {"id": "004"},   # VM (important)
            "rule": {
                "description": text,
                "id": "1000",
                "level": "5",
                "groups": ["attack", scenario]
            },
            "decoder": {"name": "auditd"},
            "full_log": text,
            "location": "test_data"
        }

        # merge extra fields
        record.update(extra)

        f.write(json.dumps(record) + "\n")

print("✅ Optimized JSONL created")
