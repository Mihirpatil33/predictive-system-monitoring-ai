import random
from datetime import datetime
import csv

def generate_log():
    cpu = random.randint(10,100)
    memory = random.randint(10,100)
    error = random.randint(0,10)

    time = datetime.now()

    return[time,cpu,memory,error]

with open("data/sample_logs.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["time","cpu","memory","error"])

    for i in range(20):
        log = generate_log()
        writer.writerow(log)



print("logs saved")
