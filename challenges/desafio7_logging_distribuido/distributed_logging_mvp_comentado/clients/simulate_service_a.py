
import requests
import random
import time
from datetime import datetime, timezone

SERVER_URL = "http://127.0.0.1:8000/logs"
TOKEN = "service-a-token"
SERVICE_NAME = "service-a"

SEVERITIES = ["INFO", "DEBUG", "WARNING", "ERROR"]

def generate_log():
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "service": SERVICE_NAME,
        "severity": random.choice(SEVERITIES),
        "message": f"Random event {random.randint(1,1000)}"
    }

def send_log():
    headers = {"Authorization": f"Token {TOKEN}"}
    log = generate_log()
    response = requests.post(SERVER_URL, json=log, headers=headers)
    print(response.status_code, response.json())

if __name__ == "__main__":
    for _ in range(10):
        send_log()
        time.sleep(1)
