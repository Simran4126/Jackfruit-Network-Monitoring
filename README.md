# Network Monitoring and Alert System Using UDP and SDN

## 1. Project Overview

The Network Monitoring and Alert System monitors CPU and memory utilization on hosts and transmits telemetry data using UDP. It combines a Python-based telemetry system, a Mininet virtual network, Open vSwitch, and a Software-Defined Networking (SDN) controller.

The telemetry server validates incoming messages, records valid metrics in a CSV file, and generates alerts when configured thresholds are reached. The SDN controller communicates with Open vSwitch using OpenFlow and collects switch port statistics.

## 2. Objectives

- Monitor CPU and memory utilization.
- Transmit telemetry data using UDP sockets.
- Validate incoming telemetry messages.
- Store telemetry records in CSV format.
- Generate alerts when resource utilization reaches configured thresholds.
- Simulate a network using Mininet.
- Use an SDN controller to manage OpenFlow switches.
- Inspect network connectivity, flow rules, and switch port statistics.

## 3. Technologies Used

- Python
- UDP sockets
- psutil
- JSON and CSV
- Mininet
- Open vSwitch
- OpenFlow 1.0
- OS-Ken SDN controller framework
- Linux

## 4. Project Structure

```text
network-monitoring-system/
├── config.py
├── requirements.txt
├── README.md
├── controller/
│   ├── __init__.py
│   └── sdn_controller.py
├── network/
│   ├── topology.py
│   └── udp_test_server.py
├── telemetry/
│   ├── agent.py
│   ├── config.py
│   └── server.py
├── tests/
│   └── test_telemetry.py
├── docs/
│   ├── architecture.md
│   ├── controller.md
│   ├── network.md
│   └── telemetry.md
└── logs/
    ├── telemetry.csv
    └── alerts.log
```

## 5. Configuration

The root `config.py` file contains the telemetry configuration:

```python
HOST_ID = "h1"
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 9999
SEND_INTERVAL = 2

CPU_THRESHOLD = 80.0
MEMORY_THRESHOLD = 80.0
```

When running an agent inside a separate Mininet host namespace, the server address must be reachable from that namespace. The root configuration above uses localhost and is suitable only when the agent and server share the same network namespace.

## 6. Installation Requirements

Install the system dependencies:

```bash
sudo apt update
sudo apt install -y python3-venv python3-pip mininet openvswitch-switch iproute2
```

Create and activate the telemetry environment:

```bash
cd ~/network-monitoring-system
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

The SDN controller uses a separate OS-Ken environment in the tested setup:

```bash
python3 -m venv ~/osken-venv
source ~/osken-venv/bin/activate
python -m pip install --upgrade pip
python -m pip install os-ken
```

If `~/osken-venv` already exists, activate it instead of recreating it.

## 7. Running the SDN Controller

Open Terminal 1 and run:

```bash
cd ~/network-monitoring-system
source ~/osken-venv/bin/activate
export PYTHONPATH="$HOME/network-monitoring-system:$PYTHONPATH"
osken-manager --ofp-tcp-listen-port 6633 controller.sdn_controller
```

Keep this terminal open while running the network.

The controller uses OpenFlow 1.0 and supports MAC learning, forwarding rules, and periodic switch port-statistics requests.

## 8. Launching the Mininet Topology

Open Terminal 2:

```bash
cd ~/network-monitoring-system
sudo mn -c
sudo python3 network/topology.py
```

The topology contains four hosts and four switches.

- h1 and h2 connect to s1.
- h3 and h4 connect to s4.
- The network provides two paths between the endpoint switches.
- Links are configured with bandwidth limits.
- Open vSwitch connects to the remote controller at `127.0.0.1:6633`.

Allow the topology's configured startup delay for spanning-tree convergence.

## 9. Testing Network Connectivity

At the `mininet>` prompt, run:

```text
pingall
h1 ping -c 2 10.0.0.4
```

Successful connectivity should show no packet loss.

Inspect the OpenFlow rules with:

```text
sh ovs-ofctl -O OpenFlow10 dump-flows s1
sh ovs-ofctl -O OpenFlow10 dump-flows s4
```

The output displays the flow rules installed on the switches.

## 10. Running the UDP Telemetry System

The telemetry system has an agent that collects resource metrics and a server that receives and records them.

For a basic same-network-namespace test, open two terminals.

Terminal 1:

```bash
cd ~/network-monitoring-system
source .venv/bin/activate
python -m telemetry.server
```

Terminal 2:

```bash
cd ~/network-monitoring-system
source .venv/bin/activate
python -m telemetry.agent
```

The root configuration uses `127.0.0.1:9999`. For a Mininet demonstration, configure the server and agents to use reachable addresses inside the appropriate host namespaces.

The topology includes `network/udp_test_server.py` for network-side UDP testing.

## 11. Running the Tests

Run the telemetry unit tests:

```bash
cd ~/network-monitoring-system
source .venv/bin/activate
python -m pytest -v tests/test_telemetry.py
```

The telemetry test suite has previously passed all 10 tests.

## 12. Output Files

### logs/telemetry.csv

Stores received telemetry records with the following fields:

- `host_id`
- `timestamp`
- `cpu_percent`
- `memory_percent`

### logs/alerts.log

Stores threshold-based alerts generated by the telemetry server.

## 13. Demonstration Workflow

The intended demonstration follows this order:

1. Start the OS-Ken SDN controller.
2. Launch the Mininet topology.
3. Confirm that the switches connect to the controller.
4. Test connectivity between the hosts.
5. Inspect OpenFlow rules and switch port statistics.
6. Start the UDP telemetry server.
7. Start telemetry agents with valid server addresses.
8. Verify that telemetry records appear in the CSV file.
9. Demonstrate threshold-based alerts.
10. Run the telemetry unit tests.

Each component should be checked independently before presenting the integrated demonstration.

## 14. Limitations and Future Enhancements

- Extend telemetry to include additional system and network metrics.
- Integrate switch statistics with host telemetry.
- Add dashboards for CPU, memory, and network activity.
- Improve alert presentation and anomaly detection.
- Perform additional end-to-end tests across the Mininet topology.

## 15. Conclusion

The project combines UDP-based telemetry, resource monitoring, threshold-based alerts, Mininet network simulation, and SDN-based switch management. It demonstrates how host monitoring and programmable network management can be explored together in a virtual network.
