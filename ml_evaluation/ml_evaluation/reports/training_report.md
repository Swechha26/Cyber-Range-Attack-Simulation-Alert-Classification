# Cyber Range ML Evaluation Report

Generated: 2026-04-24T18:55:40

## Summary

- Total records analyzed: 707
- Average model confidence: 1.00
- Average defender usefulness score: 17.2/100
- Difficulty recommendation: Easy: repeat the scenario on VM target with clearer monitored paths before increasing complexity.

## Scenario Distribution

| Predicted Scenario | Count | MITRE Technique | NICE Role Relevance |
| --- | ---: | --- | --- |
| Container Noise / Rootcheck Dominated | 600 | N/A | Cyber Defense Analyst / SOC Evaluation |
| Privilege / Authentication Activity | 57 | T1548.003, T1078 | Incident Responder / Cyber Defense Analyst |
| File Integrity Change | 48 | T1565.001 | Cyber Defense Analyst |
| Command Execution / Discovery | 2 | T1082, T1057 | Cyber Defense Analyst |

## Defender Usefulness

| Usefulness Level | Count |
| --- | ---: |
| High | 61 |
| Medium | 0 |
| Low | 46 |
| Noise | 600 |

## Target Comparison

| Agent ID | Records | Interpretation |
| --- | ---: | --- |
| 002 | 566 | Container target: expected more limited or rootcheck-dominated telemetry |
| 003 | 122 | Unmapped target |
| 004 | 19 | VM target: expected richer audit/auth/syscheck telemetry |

## Event-Level Predictions

| Time | Agent | Scenario | Confidence | Usefulness | Score | Rule | Location |
| --- | --- | --- | ---: | --- | ---: | --- | --- |
| 2026-04-09T11:04:50.356Z | 003 | Command Execution / Discovery | 1.00 | Low | 35 | 92604 | /var/log/audit/audit.log |
| 2026-04-09T13:40:53.644Z | 003 | Command Execution / Discovery | 1.00 | Low | 35 | 92604 | /var/log/audit/audit.log |
| 2026-04-08T07:17:30.351Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-10T15:54:15.724Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-08T04:27:37.360Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-10T15:54:15.723Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-08T04:53:29.454Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-08T07:17:30.384Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-08T02:33:51.948Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-07T23:00:00.390Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-11T03:59:24.842Z | 003 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-08T00:47:38.562Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-08T00:05:36.411Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-07T23:12:30.432Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-07T23:02:30.399Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-08T00:42:38.544Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-08T07:17:30.352Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-08T02:59:50.044Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-08T07:17:30.390Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-08T05:02:14.488Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-08T02:21:33.904Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-08T04:17:42.325Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-08T02:41:21.974Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-08T07:17:30.349Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-08T07:17:30.368Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-08T01:02:24.616Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-08T07:17:30.369Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-08T01:01:09.612Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-08T07:17:30.408Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-08T04:57:14.469Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-08T07:17:30.388Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-07T23:56:52.585Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-07T23:48:17.555Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-08T00:29:06.492Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-08T02:40:06.970Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-07T23:14:50.438Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-08T07:17:30.414Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-08T03:54:10.242Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-08T00:25:21.480Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-08T07:17:30.417Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-07T23:37:06.515Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-07T23:10:00.423Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-08T07:17:30.395Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-07T22:34:08.294Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-08T07:17:30.370Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-08T07:17:30.369Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-08T07:17:30.399Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-08T00:14:16.440Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-07T21:55:42.154Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-07T22:03:12.183Z | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| ... | ... | 657 more events omitted | ... | ... | ... | ... | ... |
