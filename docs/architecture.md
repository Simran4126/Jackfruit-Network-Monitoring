# Network Monitoring and Alert System

## Project Objective

To monitor network-related activity and host resource usage,
collect monitoring data, identify abnormal conditions, and
generate alerts.

## Components

### P1: Telemetry and Monitoring
- Collect host CPU and memory usage.
- Measure latency using a defined measurement method.
- Calculate packet rate using a defined measurement method.
- Send telemetry using UDP.
- Receive and parse telemetry messages.
- Store telemetry in CSV files.
- Generate alerts based on configurable thresholds.

### P2: Network Topology and Traffic
- Develop and configure the Mininet topology.
- Establish host connectivity.
- Generate network traffic for testing.

### P3: SDN Controller
- Develop the OS-Ken controller application.
- Collect switch and flow statistics using OpenFlow.
- Make the required statistics available for integration.

## Integration

- Host telemetry is sent to the monitoring server.
- Network traffic is generated using the Mininet topology.
- Switch statistics are collected by the SDN controller.
- The components are integrated to support monitoring and alerts.

## Integration Details To Be Confirmed

- Final topology and IP addresses.
- Telemetry UDP port.
- Telemetry message format.
- Switch-statistics interface.
- Alert thresholds.
