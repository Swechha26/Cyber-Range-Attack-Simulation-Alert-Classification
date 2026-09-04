# Cyber Range ML Evaluation Report

Generated: 2026-04-24T18:55:54

## Summary

- Total records analyzed: 29358
- Average model confidence: 0.85
- Average defender usefulness score: 82.1/100
- Difficulty recommendation: Hard: increase stealth, add multi-step persistence, or require correlation across audit/auth/syscheck.

## Scenario Distribution

| Predicted Scenario | Count | MITRE Technique | NICE Role Relevance |
| --- | ---: | --- | --- |
| Persistence / Config Change | 12550 | T1053.003 | Security Analyst / Incident Responder |
| Payload Delivery / File Drop | 9485 | T1105 | Cyber Defense Analyst |
| Privilege / Authentication Activity | 5959 | T1548.003, T1078 | Incident Responder / Cyber Defense Analyst |
| File Integrity Change | 782 | T1565.001 | Cyber Defense Analyst |
| Command Execution / Discovery | 582 | T1082, T1057 | Cyber Defense Analyst |

## Defender Usefulness

| Usefulness Level | Count |
| --- | ---: |
| High | 23558 |
| Medium | 0 |
| Low | 5800 |
| Noise | 0 |

## Target Comparison

| Agent ID | Records | Interpretation |
| --- | ---: | --- |
| 004 | 29358 | VM target: expected richer audit/auth/syscheck telemetry |

## Event-Level Predictions

| Time | Agent | Scenario | Confidence | Usefulness | Score | Rule | Location |
| --- | --- | --- | ---: | --- | ---: | --- | --- |
| 2026-01-01T00:00:00Z | 004 | Persistence / Config Change | 0.90 | High | 100 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Payload Delivery / File Drop | 0.82 | High | 75 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Payload Delivery / File Drop | 0.92 | Low | 35 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Privilege / Authentication Activity | 1.00 | High | 100 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Persistence / Config Change | 0.85 | High | 100 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Payload Delivery / File Drop | 0.92 | Low | 35 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Privilege / Authentication Activity | 1.00 | High | 100 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Payload Delivery / File Drop | 0.92 | Low | 35 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Privilege / Authentication Activity | 1.00 | High | 100 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Payload Delivery / File Drop | 0.92 | Low | 35 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Privilege / Authentication Activity | 1.00 | High | 100 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Persistence / Config Change | 0.85 | High | 100 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Privilege / Authentication Activity | 1.00 | High | 100 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Persistence / Config Change | 0.85 | High | 100 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Persistence / Config Change | 0.85 | High | 100 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Payload Delivery / File Drop | 0.92 | Low | 35 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Payload Delivery / File Drop | 0.82 | High | 75 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Payload Delivery / File Drop | 0.82 | High | 75 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Persistence / Config Change | 0.85 | High | 100 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Persistence / Config Change | 0.85 | High | 100 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Persistence / Config Change | 0.90 | High | 100 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Privilege / Authentication Activity | 1.00 | High | 100 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Privilege / Authentication Activity | 1.00 | High | 100 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Persistence / Config Change | 0.90 | High | 100 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Payload Delivery / File Drop | 0.82 | High | 75 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Privilege / Authentication Activity | 1.00 | High | 100 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Persistence / Config Change | 0.85 | High | 100 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Payload Delivery / File Drop | 0.82 | High | 75 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Persistence / Config Change | 0.85 | High | 100 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Privilege / Authentication Activity | 1.00 | High | 100 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Persistence / Config Change | 0.85 | High | 100 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Persistence / Config Change | 0.85 | High | 100 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Persistence / Config Change | 0.90 | High | 100 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Persistence / Config Change | 0.90 | High | 100 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Persistence / Config Change | 0.85 | High | 100 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Privilege / Authentication Activity | 1.00 | High | 100 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Persistence / Config Change | 0.90 | High | 100 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Persistence / Config Change | 0.90 | High | 100 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Privilege / Authentication Activity | 1.00 | High | 100 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Privilege / Authentication Activity | 1.00 | High | 100 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Payload Delivery / File Drop | 0.92 | Low | 35 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Payload Delivery / File Drop | 0.92 | Low | 35 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Persistence / Config Change | 0.85 | High | 100 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Payload Delivery / File Drop | 0.92 | Low | 35 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Privilege / Authentication Activity | 1.00 | High | 100 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Persistence / Config Change | 0.85 | High | 100 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Persistence / Config Change | 0.90 | High | 100 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Payload Delivery / File Drop | 0.82 | High | 75 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Persistence / Config Change | 0.90 | High | 100 | 1000 | test_data |
| 2026-01-01T00:00:00Z | 004 | Payload Delivery / File Drop | 0.82 | High | 75 | 1000 | test_data |
| ... | ... | 29308 more events omitted | ... | ... | ... | ... | ... |
