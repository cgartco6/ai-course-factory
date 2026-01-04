import csv
from datetime import datetime

def log_sale(amount):
    with open("automation_data/revenue.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), amount])
