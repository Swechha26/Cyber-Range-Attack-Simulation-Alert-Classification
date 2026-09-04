# Cyber Range ML Evaluation Report

Generated: 2026-04-23T12:53:20

## Summary

- Total records analyzed: 2300
- Average model confidence: 1.00
- Average defender usefulness score: 12.2/100
- Difficulty recommendation: Easy: repeat the scenario on VM target with clearer monitored paths before increasing complexity.

## Scenario Distribution

| Predicted Scenario | Count | MITRE Technique | NICE Role Relevance |
| --- | ---: | --- | --- |
| Container Noise / Rootcheck Dominated | 2193 | N/A | Cyber Defense Analyst / SOC Evaluation |
| Privilege / Authentication Activity | 57 | T1548.003, T1078 | Incident Responder / Cyber Defense Analyst |
| File Integrity Change | 48 | T1565.001 | Cyber Defense Analyst |
| Command Execution / Discovery | 2 | T1082, T1057 | Cyber Defense Analyst |

## Defender Usefulness

| Usefulness Level | Count |
| --- | ---: |
| High | 61 |
| Medium | 0 |
| Low | 46 |
| Noise | 2193 |

## Target Comparison

| Agent ID | Records | Interpretation |
| --- | ---: | --- |
| 002 | 2039 | Container target: expected more limited or rootcheck-dominated telemetry |
| 003 | 209 | Unmapped target |
| 004 | 52 | VM target: expected richer audit/auth/syscheck telemetry |

## Event-Level Predictions

| Time | Agent | Scenario | Confidence | Usefulness | Score | Rule | Location |
| --- | --- | --- | ---: | --- | ---: | --- | --- |
| 2026-04-09T13:40:53.644Z | 003 | Command Execution / Discovery | 1.00 | Low | 35 | 92604 | /var/log/audit/audit.log |
| 2026-04-09T11:04:50.356Z | 003 | Command Execution / Discovery | 1.00 | Low | 35 | 92604 | /var/log/audit/audit.log |
| 2026-04-11T03:59:24.842Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-11T03:59:24.842Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-11T03:59:24.842Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-11T03:59:23.841Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-11T03:59:23.841Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-11T03:59:23.841Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-11T03:59:23.841Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-11T03:59:23.841Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-11T03:59:22.840Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-11T03:59:22.840Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-11T03:59:22.840Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-11T03:59:22.840Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-11T03:59:22.840Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-11T03:59:21.840Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-11T03:59:21.840Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-11T03:59:21.839Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-11T03:59:21.839Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-11T03:59:20.839Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-11T03:59:20.838Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-10T15:54:16.725Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-10T15:54:16.724Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-10T15:54:16.724Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-10T15:54:15.724Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-10T15:54:15.724Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-10T15:54:15.724Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-10T15:54:15.724Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-10T15:54:15.724Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-10T15:54:15.724Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-10T15:54:15.723Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-10T15:54:15.723Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-10T15:54:15.723Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-10T15:54:15.723Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-10T15:54:15.723Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-10T15:54:15.723Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-10T15:54:15.723Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-10T15:54:15.723Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-10T15:54:15.723Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-10T15:54:15.723Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-10T03:48:41.246Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-10T03:48:41.246Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-10T03:48:41.246Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-10T03:48:41.246Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-10T03:48:41.246Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-10T03:48:41.246Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-10T03:48:41.245Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-10T03:48:41.245Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-10T03:48:41.245Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-10T03:48:41.245Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| ... | ... | 2250 more events omitted | ... | ... | ... | ... | ... |
