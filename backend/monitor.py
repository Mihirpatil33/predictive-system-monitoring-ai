from log_generator import generate_log
from anomaly_detector import detect_anomaly, train_model
import csv
import time
import logging
from config import CSV_PATH, SLEEP_TIME

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("log/monitor.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger()

model = train_model()

while True :

    log = generate_log()

    with open(CSV_PATH, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(log)

    logger.info(f"Log saved: {log}")

    detect_anomaly(model)
    time.sleep(SLEEP_TIME)
