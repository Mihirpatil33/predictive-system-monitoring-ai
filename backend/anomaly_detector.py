import pandas as pd 
from sklearn.ensemble import IsolationForest
import csv
import datetime

data = pd.read_csv("data/sample_logs.csv")

features = data[["cpu","memory","error"]]

model = IsolationForest(contamination=0.2)
model.fit(features)

predictions = model.predict(features)

data["anomaly"] = predictions

for i in range(len(data)):
    if data["anomaly"][i] == -1:
        print("ALERT!", data.iloc[i])