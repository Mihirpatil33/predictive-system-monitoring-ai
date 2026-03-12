import random
from datetime import datetime
import csv

def generate_log():
    cpu = random.randint(10,100)
    memory = random.randint(10,100)
    error = random.randint(0,10)

    time = datetime.now()

    return[time,cpu,memory,error]
