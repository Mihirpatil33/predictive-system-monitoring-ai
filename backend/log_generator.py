import random
from datetime import datetime
import csv
from config import CSV_PATH

def generate_log():
    cpu = random.randint(10,100)
    memory = random.randint(10,100)
    error = random.randint(0,10)

    time = datetime.now()

    return[time,cpu,memory,error]   
