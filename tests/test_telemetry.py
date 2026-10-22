import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(
    0,
    str(Path(__file__).resolve().parent.parent / "telemetry")
)

import server


class TelemetryTest(unittest.TestCase):

    def setUp(self):
        self.metrics = {
            "host_id": "test-host",
            "timestamp": "2026-10-20T12:00:00+00:00",
            "cpu_percent": 50.0,
            "memory_percent": 40.0,
        }

    def test_csv_file_is_created(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            csv_path = Path(temp_dir) / "telemetry.csv"

            with patch.object(server, "LOG_DIR", Path(temp_dir)), \
                 patch.object(server, "CSV_FILE", csv_path):

                server.prepare_files()

                self.assertTrue(csv_path.exists())

                content = csv_path.read_text()
                self.assertIn("host_id", content)
                self.assertIn("cpu_percent", content)

    def test_cpu_alert(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            alert_path = Path(temp_dir) / "alerts.log"

            with patch.object(server, "ALERT_FILE", alert_path), \
                 patch.object(server, "CPU_THRESHOLD", 80.0), \
                 patch.object(server, "MEMORY_THRESHOLD", 80.0):

                self.metrics["cpu_percent"] = 95.0

                server.check_alerts(self.metrics)

                content = alert_path.read_text()

                self.assertIn("High CPU usage", content)
                self.assertNotIn("High memory usage", content)

    def test_memory_alert(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            alert_path = Path(temp_dir) / "alerts.log"

            with patch.object(server, "ALERT_FILE", alert_path), \
                 patch.object(server, "CPU_THRESHOLD", 80.0), \
                 patch.object(server, "MEMORY_THRESHOLD", 80.0):

                self.metrics["memory_percent"] = 90.0

                server.check_alerts(self.metrics)

                content = alert_path.read_text()

                self.assertIn("High memory usage", content)
                self.assertNotIn("High CPU usage", content)

    def test_no_alert_below_threshold(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            alert_path = Path(temp_dir) / "alerts.log"

            with patch.object(server, "ALERT_FILE", alert_path), \
                 patch.object(server, "CPU_THRESHOLD", 80.0), \
                 patch.object(server, "MEMORY_THRESHOLD", 80.0):

                self.metrics["cpu_percent"] = 79.0
                self.metrics["memory_percent"] = 79.0

                alerts = server.check_alerts(self.metrics)

                self.assertEqual(alerts, [])
                self.assertFalse(alert_path.exists())

    def test_alert_at_threshold(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            alert_path = Path(temp_dir) / "alerts.log"

            with patch.object(server, "ALERT_FILE", alert_path), \
                 patch.object(server, "CPU_THRESHOLD", 80.0), \
                 patch.object(server, "MEMORY_THRESHOLD", 80.0):

                self.metrics["cpu_percent"] = 80.0

                server.check_alerts(self.metrics)

                content = alert_path.read_text()
                self.assertIn("High CPU usage", content)

    def test_valid_metrics(self):
        self.assertTrue(server.validate_metrics(self.metrics))

    def test_missing_field_is_rejected(self):
        del self.metrics["host_id"]

        self.assertFalse(server.validate_metrics(self.metrics))

    def test_invalid_metric_type_is_rejected(self):
        self.metrics["cpu_percent"] = "high"

        self.assertFalse(server.validate_metrics(self.metrics))

    def test_metric_out_of_range_is_rejected(self):
        self.metrics["cpu_percent"] = 105.0

        self.assertFalse(server.validate_metrics(self.metrics))

    def test_negative_metric_is_rejected(self):
        self.metrics["memory_percent"] = -1.0

        self.assertFalse(server.validate_metrics(self.metrics))


if __name__ == "__main__":
    unittest.main()
