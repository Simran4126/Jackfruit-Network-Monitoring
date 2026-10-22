import csv
import json
import socket
from pathlib import Path

from config import (
    SERVER_HOST,
    SERVER_PORT,
    CPU_THRESHOLD,
    MEMORY_THRESHOLD,
)

PROJECT_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = PROJECT_DIR / "logs"
CSV_FILE = LOG_DIR / "telemetry.csv"
ALERT_FILE = LOG_DIR / "alerts.log"

FIELDS = [
    "host_id",
    "timestamp",
    "cpu_percent",
    "memory_percent",
]


def validate_metrics(metrics):
    if not isinstance(metrics, dict):
        return False

    if not all(field in metrics for field in FIELDS):
        return False

    if not isinstance(metrics["host_id"], str) or not metrics["host_id"].strip():
        return False

    if not isinstance(metrics["timestamp"], str) or not metrics["timestamp"].strip():
        return False

    for field in ["cpu_percent", "memory_percent"]:
        value = metrics[field]

        if isinstance(value, bool) or not isinstance(value, (int, float)):
            return False

        if not 0 <= value <= 100:
            return False

    return True
    
    

def prepare_files():
    LOG_DIR.mkdir(exist_ok=True)

    if not CSV_FILE.exists():
        with CSV_FILE.open("w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()


def check_alerts(metrics):
    alerts = []

    if metrics["cpu_percent"] >= CPU_THRESHOLD:
        alerts.append(
            f"{metrics.get('timestamp', '')} | "
            f"Host: {metrics['host_id']} | "
            f"High CPU usage: {metrics['cpu_percent']}%"
        )

    if metrics["memory_percent"] >= MEMORY_THRESHOLD:
        alerts.append(
            f"{metrics.get('timestamp', '')} | "
            f"Host: {metrics['host_id']} | "
            f"High memory usage: {metrics['memory_percent']}%"
        )

    if alerts:
        ALERT_FILE.parent.mkdir(parents=True, exist_ok=True)

        with ALERT_FILE.open("a") as file:
            for alert in alerts:
                file.write(alert + "\n")
                print("ALERT:", alert)

    return alerts


def main():
    prepare_files()

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind((SERVER_HOST, SERVER_PORT))

        print(f"UDP server listening on {SERVER_HOST}:{SERVER_PORT}")

        while True:
            data, address = sock.recvfrom(65535)

            try:
                metrics = json.loads(data.decode("utf-8"))

                if not validate_metrics(metrics):
                    print("Invalid telemetry: missing fields or invalid values")
                    continue

                print("Received:", metrics)

                with CSV_FILE.open("a", newline="") as file:
                    writer = csv.DictWriter(file, fieldnames=FIELDS)
                    writer.writerow(metrics)

                check_alerts(metrics)

            except (
                json.JSONDecodeError,
                UnicodeDecodeError,
                TypeError,
                KeyError,
            ) as error:
                print("Invalid message:", error)


if __name__ == "__main__":
    main()
