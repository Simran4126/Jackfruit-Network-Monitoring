import json
import socket
import time
from datetime import datetime, timezone

import psutil

from config import (
    HOST_ID,
    SERVER_HOST,
    SERVER_PORT,
    SEND_INTERVAL,
)


def collect_metrics():
    return {
        "host_id": HOST_ID,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "cpu_percent": psutil.cpu_percent(interval=0.5),
        "memory_percent": psutil.virtual_memory().percent,
    }


def send_telemetry():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        while True:
            metrics = collect_metrics()

            message = json.dumps(metrics).encode("utf-8")

            sock.sendto(
                message,
                (SERVER_HOST, SERVER_PORT)
            )

            print("Sent:", message.decode("utf-8"))

            time.sleep(SEND_INTERVAL)


if __name__ == "__main__":
    try:
        send_telemetry()
    except KeyboardInterrupt:
        print("\nTelemetry agent stopped.")
