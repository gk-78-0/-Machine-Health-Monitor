Machine Health Monitor
📌 Overview

The Machine Health Monitor is a real-time monitoring system that integrates Prometheus, Grafana, and a backend service to track the performance and health of machines. It provides visualization dashboards and alerts for better insights into system health.

🚀 Features

Backend service built with Python (Flask)

Prometheus for metrics collection

Grafana for visualization and dashboards

Docker Compose for containerized deployment

Machine health simulator for testing

🛠️ Tech Stack

Python (Flask)

Prometheus

Grafana

Docker & Docker Compose

📂 Project Structure
├── backend/                 # Flask app (API for machine health data)
│   ├── app.py
│   └── requirements.txt
├── grafana/                 # Grafana provisioning and dashboards
│   └── provisioning/dashboards/dashboard.json
├── prometheus/              # Prometheus configuration
│   └── prometheus.yml
├── simulator/               # Machine data simulator
│   └── simulate.sh
├── Dockerfile               # Base Dockerfile
├── Dockerfile.backend       # Backend-specific Dockerfile
├── Dockerfile.simulator     # Simulator-specific Dockerfile
├── docker-compose.yml       # Orchestration of services

⚡ Getting Started
1. Clone the repository
git clone https://github.com/your-username/Machine-Health-Monitor.git
cd Machine-Health-Monitor

2. Run with Docker Compose
docker-compose up --build
<img width="818" height="490" alt="docker compose " src="https://github.com/user-attachments/assets/099806a1-8a62-48c4-8ff7-490c2a9ef521" />
3. Access the services

Backend API → http://localhost:5000

Prometheus → http://localhost:9090

Grafana → http://localhost:3000

Default Grafana login:

Username: admin

Password: admin

📊 Dashboard

Grafana provides a real-time machine health dashboard with metrics from Prometheus.
<img width="1038" height="575" alt="image" src="https://github.com/user-attachments/assets/3a1f74e9-e1d6-4a34-9460-2d181ca86921" />

🔮 Future Enhancements

Add alerting rules in Prometheus

Expand simulator with more machine parameters

Integrate anomaly detection with ML

📜 License

This project is licensed under the MIT License.
