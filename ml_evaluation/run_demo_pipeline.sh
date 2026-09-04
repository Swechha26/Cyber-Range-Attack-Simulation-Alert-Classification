#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

python3 ml_evaluation/wazuh_ml_evaluator.py train \
  --input ml_evaluation/data/sample_alerts.jsonl \
  --model ml_evaluation/model.json

python3 ml_evaluation/wazuh_ml_evaluator.py report \
  --input ml_evaluation/data/sample_alerts.jsonl \
  --model ml_evaluation/model.json \
  --output ml_evaluation/reports/sample_report.md

printf '\nReport generated at: ml_evaluation/reports/sample_report.md\n'
printf 'Preview:\n\n'
sed -n '1,90p' ml_evaluation/reports/sample_report.md
