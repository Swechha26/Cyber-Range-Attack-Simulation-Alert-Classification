# Cyber Range ML Evaluation Report

Generated: 2026-04-23T11:50:22

## Summary

- Total records analyzed: 10
- Average model confidence: 0.99
- Average defender usefulness score: 52.5/100
- Difficulty recommendation: Medium: continue with similar ATT&CK technique and add one extra investigation step.

## Scenario Distribution

| Predicted Scenario | Count | MITRE Technique | NICE Role Relevance |
| --- | ---: | --- | --- |
| Command Execution / Discovery | 2 | T1082, T1057 | Cyber Defense Analyst |
| Privilege / Authentication Activity | 2 | T1548.003, T1078 | Incident Responder / Cyber Defense Analyst |
| Persistence / Config Change | 2 | T1053.003 | Security Analyst / Incident Responder |
| Container Noise / Rootcheck Dominated | 2 | N/A | Cyber Defense Analyst / SOC Evaluation |
| File Integrity Change | 1 | T1565.001 | Cyber Defense Analyst |
| Payload Delivery / File Drop | 1 | T1105 | Cyber Defense Analyst |

## Defender Usefulness

| Usefulness Level | Count |
| --- | ---: |
| High | 6 |
| Medium | 0 |
| Low | 2 |
| Noise | 2 |

## Target Comparison

| Agent ID | Records | Interpretation |
| --- | ---: | --- |
| 004 | 8 | VM target: expected richer audit/auth/syscheck telemetry |
| 002 | 2 | Container target: expected more limited or rootcheck-dominated telemetry |

## Event-Level Predictions

| Time | Agent | Scenario | Confidence | Usefulness | Score | Rule | Location |
| --- | --- | --- | ---: | --- | ---: | --- | --- |
| 2026-04-23T09:00:00Z | 004 | File Integrity Change | 1.00 | High | 70 | 550 | syscheck |
| 2026-04-23T09:02:00Z | 004 | Command Execution / Discovery | 1.00 | Low | 35 | 80792 | /var/log/audit/audit.log |
| 2026-04-23T09:03:00Z | 004 | Command Execution / Discovery | 1.00 | Low | 35 | 80792 | /var/log/audit/audit.log |
| 2026-04-23T09:05:00Z | 004 | Privilege / Authentication Activity | 1.00 | High | 70 | 5402 | /var/log/auth.log |
| 2026-04-23T09:06:00Z | 004 | Privilege / Authentication Activity | 1.00 | High | 70 | 5502 | /var/log/auth.log |
| 2026-04-23T09:10:00Z | 004 | Payload Delivery / File Drop | 1.00 | High | 75 | 554 | syscheck |
| 2026-04-23T09:11:00Z | 004 | Persistence / Config Change | 0.99 | High | 70 | 550 | syscheck |
| 2026-04-23T09:12:00Z | 004 | Persistence / Config Change | 0.92 | High | 80 | 5402 | /var/log/auth.log |
| 2026-04-23T09:15:00Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T09:16:00Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
