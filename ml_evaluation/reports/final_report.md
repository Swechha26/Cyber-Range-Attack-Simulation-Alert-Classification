# Cyber Range ML Evaluation Report

Generated: 2026-04-24T18:23:34

## Summary

- Total records analyzed: 5000
- Average model confidence: 1.00
- Average defender usefulness score: 24.2/100
- Difficulty recommendation: Easy: repeat the scenario on VM target with clearer monitored paths before increasing complexity.

## Scenario Distribution

| Predicted Scenario | Count | MITRE Technique | NICE Role Relevance |
| --- | ---: | --- | --- |
| Container Noise / Rootcheck Dominated | 2193 | N/A | Cyber Defense Analyst / SOC Evaluation |
| Command Execution / Discovery | 1934 | T1082, T1057 | Cyber Defense Analyst |
| File Integrity Change | 724 | T1565.001 | Cyber Defense Analyst |
| Privilege / Authentication Activity | 111 | T1548.003, T1078 | Incident Responder / Cyber Defense Analyst |
| Payload Delivery / File Drop | 31 | T1105 | Cyber Defense Analyst |
| Persistence / Config Change | 7 | T1053.003 | Security Analyst / Incident Responder |

## Defender Usefulness

| Usefulness Level | Count |
| --- | ---: |
| High | 61 |
| Medium | 0 |
| Low | 2715 |
| Noise | 2224 |

## Target Comparison

| Agent ID | Records | Interpretation |
| --- | ---: | --- |
| 003 | 2626 | Unmapped target |
| 002 | 2039 | Container target: expected more limited or rootcheck-dominated telemetry |
| 004 | 331 | VM target: expected richer audit/auth/syscheck telemetry |
| 000 | 4 | Unmapped target |

## Event-Level Predictions

| Time | Agent | Scenario | Confidence | Usefulness | Score | Rule | Location |
| --- | --- | --- | ---: | --- | ---: | --- | --- |
| 2026-04-13T09:26:34.943Z | 000 | Privilege / Authentication Activity | 0.99 | Low | 25 | 502 | wazuh-monitord |
| 2026-04-11T07:33:46.465Z | 003 | Privilege / Authentication Activity | 1.00 | Low | 25 | 504 | wazuh-monitord |
| 2026-04-11T07:15:56.411Z | 003 | File Integrity Change | 1.00 | Low | 35 | 591 | logcollector |
| 2026-04-11T07:10:36.396Z | 003 | File Integrity Change | 1.00 | Low | 35 | 591 | logcollector |
| 2026-04-11T07:04:16.376Z | 003 | File Integrity Change | 1.00 | Low | 35 | 591 | logcollector |
| 2026-04-11T06:58:56.362Z | 003 | File Integrity Change | 1.00 | Low | 35 | 591 | logcollector |
| 2026-04-11T06:52:31.345Z | 003 | File Integrity Change | 1.00 | Low | 35 | 591 | logcollector |
| 2026-04-11T06:51:56.343Z | 003 | Command Execution / Discovery | 1.00 | Low | 35 | 80730 | /var/log/audit/audit.log |
| 2026-04-11T06:51:56.342Z | 003 | Command Execution / Discovery | 1.00 | Low | 35 | 80730 | /var/log/audit/audit.log |
| 2026-04-11T06:51:56.342Z | 003 | Command Execution / Discovery | 1.00 | Low | 35 | 80730 | /var/log/audit/audit.log |
| 2026-04-11T06:51:56.342Z | 003 | Command Execution / Discovery | 1.00 | Low | 35 | 80730 | /var/log/audit/audit.log |
| 2026-04-11T06:46:06.324Z | 003 | File Integrity Change | 1.00 | Low | 35 | 591 | logcollector |
| 2026-04-11T06:39:46.305Z | 003 | File Integrity Change | 1.00 | Low | 35 | 591 | logcollector |
| 2026-04-11T06:34:26.289Z | 003 | File Integrity Change | 1.00 | Low | 35 | 591 | logcollector |
| 2026-04-11T06:27:56.270Z | 003 | File Integrity Change | 1.00 | Low | 35 | 591 | logcollector |
| 2026-04-11T06:22:36.255Z | 003 | File Integrity Change | 1.00 | Low | 35 | 591 | logcollector |
| 2026-04-11T06:17:16.238Z | 003 | File Integrity Change | 1.00 | Low | 35 | 591 | logcollector |
| 2026-04-11T06:10:56.220Z | 003 | File Integrity Change | 1.00 | Low | 35 | 591 | logcollector |
| 2026-04-11T06:04:36.202Z | 003 | File Integrity Change | 1.00 | Low | 35 | 591 | logcollector |
| 2026-04-11T05:59:16.184Z | 003 | File Integrity Change | 1.00 | Low | 35 | 591 | logcollector |
| 2026-04-11T05:52:46.164Z | 003 | File Integrity Change | 1.00 | Low | 35 | 591 | logcollector |
| 2026-04-11T05:46:26.145Z | 003 | File Integrity Change | 1.00 | Low | 35 | 591 | logcollector |
| 2026-04-11T05:41:06.131Z | 003 | File Integrity Change | 1.00 | Low | 35 | 591 | logcollector |
| 2026-04-11T05:34:36.112Z | 003 | File Integrity Change | 1.00 | Low | 35 | 591 | logcollector |
| 2026-04-11T05:28:16.092Z | 003 | File Integrity Change | 1.00 | Low | 35 | 591 | logcollector |
| 2026-04-11T05:22:56.078Z | 003 | File Integrity Change | 1.00 | Low | 35 | 591 | logcollector |
| 2026-04-11T05:17:36.063Z | 003 | File Integrity Change | 1.00 | Low | 35 | 591 | logcollector |
| 2026-04-11T05:11:06.045Z | 003 | File Integrity Change | 1.00 | Low | 35 | 591 | logcollector |
| 2026-04-11T05:04:46.026Z | 003 | File Integrity Change | 1.00 | Low | 35 | 591 | logcollector |
| 2026-04-11T04:59:26.009Z | 003 | File Integrity Change | 1.00 | Low | 35 | 591 | logcollector |
| 2026-04-11T04:53:05.991Z | 003 | File Integrity Change | 1.00 | Low | 35 | 591 | logcollector |
| 2026-04-11T04:46:35.973Z | 003 | File Integrity Change | 1.00 | Low | 35 | 591 | logcollector |
| 2026-04-11T04:41:15.957Z | 003 | File Integrity Change | 1.00 | Low | 35 | 591 | logcollector |
| 2026-04-11T04:34:55.939Z | 003 | File Integrity Change | 1.00 | Low | 35 | 591 | logcollector |
| 2026-04-11T04:28:25.919Z | 003 | File Integrity Change | 1.00 | Low | 35 | 591 | logcollector |
| 2026-04-11T04:23:05.903Z | 003 | File Integrity Change | 1.00 | Low | 35 | 591 | logcollector |
| 2026-04-11T04:17:45.889Z | 003 | File Integrity Change | 1.00 | Low | 35 | 591 | logcollector |
| 2026-04-11T04:11:25.870Z | 003 | File Integrity Change | 1.00 | Low | 35 | 591 | logcollector |
| 2026-04-11T04:05:04.857Z | 003 | File Integrity Change | 1.00 | Low | 35 | 591 | logcollector |
| 2026-04-11T04:01:49.849Z | 003 | File Integrity Change | 1.00 | Low | 35 | 591 | logcollector |
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
| ... | ... | 4950 more events omitted | ... | ... | ... | ... | ... |
