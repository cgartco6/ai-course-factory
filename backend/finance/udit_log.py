from datetime import datetime

def log(event):
    with open("automation_data/audit.log", "a") as f:
        f.write(f"{datetime.now()} - {event}\n")
