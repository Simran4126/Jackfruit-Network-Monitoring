# P1: Telemetry and Monitoring

## Objective
Collect host resource metrics and send them to a UDP monitoring server.

## Metrics
- CPU utilization
- Memory utilization

## Communication
The agent serializes telemetry as JSON and sends it using UDP.

## Monitoring Server
The server receives telemetry, parses JSON, and writes readings to CSV.

## Alerts
The server compares CPU and memory readings with configurable thresholds.

## Output Files
- logs/telemetry.csv
- logs/alerts.log

## Tests
- Local UDP communication
- JSON parsing
- CSV file creation
- CPU threshold alert
- Memory threshold alert

## Limitations
- The initial version is tested locally.
- Network latency and packet-rate measurement are not yet implemented.
- Mininet integration has not yet been completed.
- Switch-level statistics require integration with the SDN controller.
