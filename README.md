# AI-Based Predictive System Monitoring

This project is a backend-style monitoring system that generates system logs, detects anomalies using Machine Learning, and reports risk levels in real time.

The goal of this project is to simulate how real monitoring tools work in production environments.

---

## Features

- Log generation with CPU, memory, and error metrics
- CSV-based log storage
- Anomaly detection using Isolation Forest (Scikit-learn)
- Risk level classification (NORMAL / WARNING / CRITICAL / ANOMALY)
- Continuous monitoring loop
- Configurable settings using config file
- Console and file logging
- Clean modular backend structure

---

## Project Structure

predictive-system-monitoring-ai/
│
├── backend/
│ ├── monitor.py
│ ├── log_generator.py
│ ├── anomaly_detector.py
│ ├── config.py
│
├── data/
│ └── sample_logs.csv
│
├── logs/
│ └── monitor.log
│
├── .gitignore
└── README.md


---

## How it works

1. Log generator creates fake system logs
2. Logs are stored in CSV
3. ML model detects anomalies
4. Risk level is assigned
5. Monitor runs continuously
6. Alerts are logged to file and console

---

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Logging
- Git

---

## Future Improvements

- Save and reuse ML model
- API for monitoring
- Dashboard UI
- Real log integration
- Email / webhook alerts