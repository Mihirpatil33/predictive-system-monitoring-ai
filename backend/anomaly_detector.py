import pandas as pd 
from sklearn.ensemble import IsolationForest
import csv
import datetime
import logging
from backend.config import CSV_PATH, CONTAMINATION
from backend.model_manager import save_model, load_model

logger = logging.getLogger()

def train_model():

    model = load_model()

    if model is not None:
        return model

    data = pd.read_csv(CSV_PATH)

    features = data[["cpu", "memory", "error"]]

    model = IsolationForest(contamination=CONTAMINATION)

    model.fit(features)

    save_model(model)

    return model


def detect_anomaly(model):

    data = pd.read_csv("data/sample_logs.csv")

    features = data[["cpu", "memory", "error"]]

    predictions = model.predict(features)

    data["anomaly"] = predictions

    data["risk"] = "NORMAL"

    for i in range(len(data)):

        cpu = data.loc[i, "cpu"]
        memory = data.loc[i, "memory"]
        error = data.loc[i, "error"]

        if cpu > 85 or memory > 90:
            data.loc[i, "risk"] = "WARNING"

        if error > 7:
            data.loc[i, "risk"] = "CRITICAL"

        if data.loc[i, "anomaly"] == -1:
            data.loc[i, "risk"] = "ANOMALY"

    last_row = data.iloc[-1]

    risk = last_row["risk"]

    if risk == "ANOMALY":
        logger.warning(f"ANOMALY DETECTED: {last_row.to_dict()}")

    elif risk == "CRITICAL":
        logger.warning(f"CRITICAL STATE: {last_row.to_dict()}")

    elif risk == "WARNING":
        logger.info(f"WARNING STATE: {last_row.to_dict()}")

    else:
        logger.info("System normal")