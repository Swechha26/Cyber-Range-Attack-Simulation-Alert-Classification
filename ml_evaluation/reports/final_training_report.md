# Cyber Range ML Evaluation Report

Generated: 2026-04-23T16:14:26

## Summary

- Total records analyzed: 137
- Average model confidence: 0.99
- Average defender usefulness score: 26.7/100
- Difficulty recommendation: Easy: repeat the scenario on VM target with clearer monitored paths before increasing complexity.

## Scenario Distribution

| Predicted Scenario | Count | MITRE Technique | NICE Role Relevance |
| --- | ---: | --- | --- |
| Container Noise / Rootcheck Dominated | 99 | N/A | Cyber Defense Analyst / SOC Evaluation |
| Privilege / Authentication Activity | 28 | T1548.003, T1078 | Incident Responder / Cyber Defense Analyst |
| File Integrity Change | 4 | T1565.001 | Cyber Defense Analyst |
| Payload Delivery / File Drop | 3 | T1105 | Cyber Defense Analyst |
| Persistence / Config Change | 3 | T1053.003 | Security Analyst / Incident Responder |

## Defender Usefulness

| Usefulness Level | Count |
| --- | ---: |
| High | 37 |
| Medium | 0 |
| Low | 0 |
| Noise | 100 |

## Target Comparison

| Agent ID | Records | Interpretation |
| --- | ---: | --- |
| 002 | 109 | Container target: expected more limited or rootcheck-dominated telemetry |
| 001 | 28 | Unmapped target |

## Event-Level Predictions

| Time | Agent | Scenario | Confidence | Usefulness | Score | Rule | Location |
| --- | --- | --- | ---: | --- | ---: | --- | --- |
| 2026-04-23T10:02:45.410+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T10:08:53.047+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T09:12:32.072+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T10:07:39.951+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T09:29:41.902+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T09:23:34.645+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T09:30:55.019+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T10:26:01.052+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T10:40:42.377+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T09:52:57.196+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T09:52:57.164+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T10:05:12.257+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T09:28:28.468+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T10:23:34.244+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T09:51:44.101+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T09:41:55.744+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T09:54:11.065+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T10:19:54.115+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T10:23:34.276+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T09:23:34.251+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T10:02:45.013+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T10:12:33.572+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T10:21:07.451+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T10:21:07.872+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T10:03:58.557+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T09:33:21.999+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T10:22:20.846+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T09:51:43.711+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T10:02:44.980+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T09:19:53.541+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T10:40:42.795+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T10:26:01.083+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T09:13:45.962+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T09:29:41.502+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T10:40:42.410+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T09:13:45.994+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T09:26:01.455+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T10:27:14.437+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T09:12:32.462+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T09:17:26.657+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T09:35:49.063+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T09:59:04.471+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T10:37:02.000+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T09:43:09.645+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T09:56:37.552+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T09:44:22.738+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T10:10:06.540+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T10:00:18.044+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T09:44:23.163+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| 2026-04-23T09:46:49.711+0000 | 002 | Container Noise / Rootcheck Dominated | 1.00 | Noise | 10 | 510 | rootcheck |
| ... | ... | 87 more events omitted | ... | ... | ... | ... | ... |
