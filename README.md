# Network Monitoring and Alert System

## 1. Project Overview

The Network Monitoring and Alert System is designed to monitor network-related activity and system resource usage. It combines UDP-based telemetry, a virtual network created using Mininet, and Software-Defined Networking (SDN).

The system collects CPU and memory utilization metrics, transfers the collected data using UDP, records the received metrics, and generates alerts when configured thresholds are reached.

The project also aims to use an SDN controller to communicate with network switches and obtain network traffic statistics.

## 2. Objectives

- Monitor CPU and memory utilization.
- Collect and transmit telemetry data using UDP sockets.
- Receive and validate telemetry messages.
- Store collected metrics in a CSV file.
- Generate alerts when configured thresholds are reached.
- Create a virtual network using Mininet.
- Explore SDN-based network management using OpenFlow.
- Integrate system monitoring with network traffic monitoring.

## 3. Technologies Used

- Python
- UDP sockets
- psutil
- CSV
- JSON
- Mininet
- Open vSwitch
- Software-Defined Networking (SDN)
- OpenFlow
- Linux

The exact controller framework and its dependencies will be documented after the controller implementation is integrated.

## 4. Project Structure

```text
network-monitoring-system/
├── config.py
├── topology.py
├── requirements.txt
├── README.md
├── telemetry/
│   ├── agent.py
│   ├── config.py
│   └── server.py
├── tests/
│   └── test_telemetry.py
├── logs/
│   ├── telemetry.csv
│   └── alerts.log
├── docs/
│   ├── architecture.md
│   ├── p1-telemetry.md
│   ├── p2-network.md
│   └── p3-controller.md
└── presentation/
    └── screenshots/
```

The controller files and additional documentation may be added when the SDN controller implementation is received and integrated.

## 5. Installation and Setup

### Step 1: Navigate to the project directory

```bash
cd ~/network-monitoring-system
```

### Step 2: Create a virtual environment

```bash
python3 -m venv .venv
```

### Step 3: Activate the virtual environment

```bash
source .venv/bin/activate
```

### Step 4: Install Python dependencies

```bash
python -m pip install -r requirements.txt
```

Mininet and Open vSwitch require separate system-level setup. The SDN controller may also require additional packages depending on the framework used.

## 6. Running the Telemetry System

Open two terminals in the project directory.

### Terminal 1: Start the UDP server

```bash
cd ~/network-monitoring-system
source .venv/bin/activate
python -m telemetry.server
```

The server receives telemetry messages and records valid metrics in the logs directory.

### Terminal 2: Start the telemetry agent

```bash
cd ~/network-monitoring-system
source .venv/bin/activate
python -m telemetry.agent
```

The agent collects CPU and memory utilization and sends the metrics to the configured UDP server.

The current configuration uses localhost. This is suitable for testing the agent and server in the same network namespace. The configuration must be updated if the agent runs inside a separate Mininet host namespace.

Press Ctrl+C to stop the agent or server.

## 7. Running the Tests

Activate the virtual environment and run:

```bash
cd ~/network-monitoring-system
source .venv/bin/activate
python -m pytest -v tests/test_telemetry.py
```

The tests check metric validation, CSV file creation, and alert-generation behavior.

The current telemetry test suite has passed all 10 tests.

## 8. Output Files

### telemetry.csv

The file stores the collected telemetry data.

The fields include:

- host_id
- timestamp
- cpu_percent
- memory_percent

### alerts.log

The file records alerts generated when CPU or memory utilization reaches the configured thresholds.

## 9. Mininet Network

The project includes a topology.py file intended to create four hosts and four switches connected through two paths between h1 and h4.

The topology and its connectivity must be tested with the selected SDN controller before the complete network demonstration.

## 10. SDN Controller

The SDN controller component is intended to communicate with Open vSwitch using OpenFlow and support the collection of network traffic statistics.

The controller framework, installation requirements, launch command, and flow-statistics demonstration will be documented after the controller implementation is integrated.

## 11. Testing and Demonstration

The planned demonstration includes:

1. Starting the SDN controller.
2. Launching the Mininet topology.
3. Checking network connectivity.
4. Starting the UDP telemetry server.
5. Starting one or more telemetry agents.
6. Displaying recorded telemetry metrics.
7. Demonstrating threshold-based alerts.
8. Displaying SDN flow statistics.

The complete demonstration will be considered successful only after the components have been integrated and tested together.

## 12. Future Enhancements

- Add additional telemetry metrics.
- Improve the presentation of alerts.
- Integrate network traffic statistics with telemetry data.
- Add visualization of CPU, memory, and network activity.
- Improve anomaly detection and monitoring capabilities.

## 13. Conclusion

The project demonstrates the use of UDP communication for telemetry collection and the use of SDN concepts for network management.

The intended integrated system combines resource monitoring, alert generation, virtual network testing, and SDN-based traffic monitoring.
