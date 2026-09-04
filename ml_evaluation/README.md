# ML-Assisted Cyber Range Evaluation

This module adds the thesis extension:

```text
Wazuh/Kibana Logs -> Feature Extraction -> ML Classification
-> Detection Usefulness Score -> Automated Report / Difficulty Recommendation
```

It is designed for your Caldera + Wazuh + Elasticsearch + Kibana cyber range. The model classifies Wazuh alerts into scenario types and generates a defender-focused report.

## Scenario Classes

- `file_integrity`
- `command_execution`
- `privilege_activity`
- `payload_drop`
- `persistence_change`
- `container_noise`

## Demo With Sample Data

Run from `/home/diat/cyber-range`:

```bash
python3 ml_evaluation/wazuh_ml_evaluator.py train \
  --input ml_evaluation/data/sample_alerts.jsonl \
  --model ml_evaluation/model.json

python3 ml_evaluation/wazuh_ml_evaluator.py report \
  --input ml_evaluation/data/sample_alerts.jsonl \
  --model ml_evaluation/model.json \
  --output ml_evaluation/reports/sample_report.md
```

Open the generated report:

```bash
sed -n '1,200p' ml_evaluation/reports/sample_report.md
```

## Export Recent Logs From Elasticsearch

If Elasticsearch is available on the host:

```bash
python3 ml_evaluation/wazuh_ml_evaluator.py export-es \
  --url http://localhost:9200 \
  --index 'wazuh-alerts-*' \
  --minutes 120 \
  --size 500 \
  --output ml_evaluation/data/recent_wazuh_alerts.jsonl
```

Useful filters:

```bash
python3 ml_evaluation/wazuh_ml_evaluator.py export-es \
  --query 'agent.id:004 AND (/etc/hosts OR sudo OR PAM OR payload_test.sh OR /etc/crontab)' \
  --output ml_evaluation/data/vm_scenario_alerts.jsonl
```

Then generate a report:

```bash
python3 ml_evaluation/wazuh_ml_evaluator.py report \
  --input ml_evaluation/data/recent_wazuh_alerts.jsonl \
  --model ml_evaluation/model.json \
  --output ml_evaluation/reports/latest_report.md
```

## Thesis Claim

Use this wording:

> An ML-assisted evaluation layer was added to classify scenario-related alerts and support automated defender-evidence scoring. This moves the cyber range from manual log inspection toward automated assessment and future adaptive learning.

## What This Does Not Claim

This is not a replacement for Wazuh detection rules. It is an automation and evaluation layer over Wazuh/Kibana telemetry. It supports classification, usefulness scoring, report generation, and future difficulty recommendation.
