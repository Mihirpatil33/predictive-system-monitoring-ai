from log_generator import generate_log
from anomaly_detector import detect_anomaly, train_model
import csv
import time
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger()

model = train_model()

while True :

    log = generate_log()

    with open("data/sample_logs.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(log)

    logger.info(f"Log saved: {log}")

    detect_anomaly(model)
    time.sleep(3)
