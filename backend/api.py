from fastapi import FastAPI
import pandas as pd
from backend.config import CSV_PATH

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Monitoring API is running"}


@app.get("/latest")
def get_latest():

    data = pd.read_csv(CSV_PATH)

    if len(data) == 0:
        return {"message": "No data available"}

    last_row = data.iloc[-1]

    return last_row.to_dict()


@app.get("/logs")
def get_logs(limit: int = 10):

    data = pd.read_csv(CSV_PATH)

    if len(data) == 0:
        return {"message": "No logs available"}

    recent_logs = data.tail(limit)

    return recent_logs.to_dict(orient="records")

@app.get("/health")
def health_check():
    return {"status": "ok"}