import pandas as pd 
from sklearn.ensemble import IsolationForest
import csv
import datetime
import logging

logger = logging.getLogger()

def train_model():
    data = pd.read_csv("data/sample_logs.csv")

    features = data[["cpu","memory","error"]]

    model = IsolationForest(contamination=0.2)
    model.fit(features)

    return model


def detect_anomaly(model):

    data = pd.read_csv("data/sample_logs.csv")

    features = data[["cpu", "memory", "error"]]

    predictions = model.predict(features)

    data["anomaly"] = predictions

    last_row = data.iloc[-1]

    if last_row["anomaly"] == -1:
        logger.warning(
            f"ANOMALY DETECTED: {last_row.to_dict()}"
        )