Project Title:
Adversary Attack Simulation and Telemetry-Based Detection in a Cyber Range using Lightweight Alert Classification

Author:
A Swechha Sonal
M.Tech Cyber Security

Project Overview:
This project presents the implementation of a telemetry-based cyber range integrating MITRE Caldera, Wazuh, Elasticsearch, Kibana, Prometheus, and lightweight Machine Learning techniques for adversary attack simulation, telemetry collection, alert monitoring, detection analysis, and classification of security alerts.

The cyber range environment is designed to simulate real-world adversarial activities using MITRE ATT&CK-based attack techniques. Telemetry generated during attack execution is collected and monitored through Wazuh and the ELK Stack (Elasticsearch and Kibana). The collected alerts and logs are further evaluated using lightweight Machine Learning models for alert classification and detection analysis.

Main Objectives:
1. Simulate adversarial attacks using MITRE Caldera.
2. Collect telemetry and security events using Wazuh.
3. Visualize alerts and logs using Kibana dashboards.
4. Monitor infrastructure and services using Prometheus.
5. Evaluate alerts and telemetry using lightweight ML-based classification.
6. Analyze attack detection effectiveness in a controlled cyber range environment.

Technologies Used:
- MITRE Caldera
- Wazuh
- Elasticsearch
- Kibana
- Prometheus
- Docker & Docker Compose
- Python
- Flask
- Machine Learning Model

Main Components:

1. MITRE Caldera
   - Adversary emulation framework
   - Attack operation execution
   - MITRE ATT&CK technique simulation

2. Wazuh
   - Telemetry collection
   - Security monitoring
   - SIEM-based alert generation

3. Elasticsearch
   - Centralized log indexing and storage

4. Kibana
   - Dashboard visualization
   - Alert monitoring and analytics

5. Prometheus
   - Service and infrastructure monitoring

6. Flask Control Layer
   - Backend orchestration
   - API integration and automation

7. Machine Learning Evaluation
   - Alert classification
   - Telemetry analysis
   - Detection evaluation

Project Folder Structure:
- control-layer/
- control_layer/
- Cyber-Range/
- ml_evaluation/
- prometheus/
- Wazuh/
- Elastic_Kibana/

Important Files Included:
- Python source code
- Docker compose configurations
- YAML/YML configuration files
- JSON model files
- CSV datasets
- Prometheus configuration
- Wazuh configuration
- Elasticsearch and Kibana configuration files

Execution Steps:
1. Start Docker services using docker-compose.
2. Launch MITRE Caldera server.
3. Configure Wazuh agents and monitoring services.
4. Access Elasticsearch and Kibana dashboards.
5. Execute attack operations using Caldera.
6. Collect telemetry and security alerts.
7. Run ML evaluation scripts from the ml_evaluation directory.
8. Analyze alert classification and detection performance.

Purpose of the Project:
The project demonstrates adversarial attack simulation, telemetry-based monitoring, SIEM integration, alert visualization, and lightweight ML-assisted alert classification within a containerized cyber range environment for cybersecurity experimentation and evaluation.

Source Code Contents:
- Attack simulation scripts
- Control layer implementation
- ML evaluation scripts
- Dataset files
- Docker deployment files
- Monitoring configurations
- Detection and telemetry analysis components

Flow :
Final_Cyber_Range_Source
├── control-layer
│   ├── app.py
│   ├── Dockerfile
│   └── flask_app
│       ├── app.py
│       └── Dockerfile
├── control_layer
│   └── control_layer.py
├── Cyber-Range
│   ├── ca
│   │   ├── intermediate
│   │   ├── openssl_csr_san.cnf
│   │   ├── openssl_root.cnf
│   │   └── scripts
│   ├── README.md
│   ├── rootdns
│   │   ├── bind
│   │   └── scripts
│   ├── rts
│   │   ├── backbonerouters
│   │   ├── Profiles
│   │   └── scripts
│   ├── SI-Router
│   │   └── Scripts
│   ├── trafficgen
│   │   ├── buildcompose.sh
│   │   ├── Dockerfile
│   │   ├── emailerlist.txt
│   │   ├── killtrafficgen.sh
│   │   ├── starttrafficgen.sh
│   │   └── TG
│   ├── ubuntubuild.sh
│   ├── WebHost
│   │   └── scripts
│   └── webservices
│       ├── drawio
│       ├── ms_sites
│       ├── ntp
│       ├── owncloud
│       ├── pastebin
│       ├── redbook
│       └── scripts
├── docker-compose.yml
├── Elastic_Kibana
│   ├── elasticsearch.yml
│   └── kibana.yml
├── ml_evaluation
│   ├── csv_to_jsonl.py
│   ├── data
│   │   ├── Data.csv
│   │   ├── fresh_labelled
│   │   ├── labelled
│   │   ├── raw
│   │   ├── sample_alerts.jsonl
│   │   └── test.jsonl
│   ├── Data.csv
│   ├── ml_evaluation
│   │   └── reports
│   ├── model_balanced.json
│   ├── model_final.json
│   ├── model.json
│   ├── model_real.json
│   ├── model_strong.json
│   ├── README.md
│   ├── reports
│   │   ├── balanced_training_report.md
│   │   ├── final_report.md
│   │   ├── final_training_report.md
│   │   ├── real_training_report.md
│   │   ├── sample_report.md
│   │   ├── test_report_balanced.md
│   │   ├── test_report_final.md
│   │   ├── test_report_improved.md
│   │   ├── test_report.md
│   │   └── training_report.md
│   ├── run_demo_pipeline.sh
│   ├── split_data.py
│   ├── test_file
│   ├── train_file
│   └── wazuh_ml_evaluator.py
├── prometheus
│   └── prometheus.yml
├── README.txt
└── Wazuh
    └── ossec.conf

40 directories, 46 files


Declaration:
This source code package is submitted as part of the M.Tech Cyber Security project work at Defence Institute of Advanced Technology (DIAT), Pune, for academic and research purposes.
