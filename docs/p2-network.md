# P2: Virtual Network and Mininet Topology

## 1. Introduction

This component uses Mininet to create a software-based virtual network containing multiple hosts and switches.

The network is intended to support connectivity testing and provide a test environment for the SDN controller.

## 2. Topology Design

The current topology.py file defines four hosts:

- h1
- h2
- h3
- h4

It also defines four switches:

- s1
- s2
- s3
- s4

Each host is connected to one switch.

## 3. Host Addressing

The current topology assigns the following IP addresses:

| Host | IP address |
|---|---|
| h1 | 10.0.0.1/24 |
| h2 | 10.0.0.2/24 |
| h3 | 10.0.0.3/24 |
| h4 | 10.0.0.4/24 |

## 4. Switch Connections

The topology defines the following host-to-switch connections:

- h1 connects to s1.
- h2 connects to s2.
- h3 connects to s3.
- h4 connects to s4.

The switches are connected as follows:

- s1 connects to s2.
- s2 connects to s4.
- s1 connects to s3.
- s3 connects to s4.

## 5. Intended Paths

The topology provides two intended paths between h1 and h4.

Path 1:

h1 → s1 → s2 → s4 → h4

Path 2:

h1 → s1 → s3 → s4 → h4

Having two physical paths does not automatically guarantee failover or load balancing. Forwarding behavior depends on the controller and switch configuration.

## 6. SDN Controller Connection

The current topology.py file attempts to connect to a remote controller at:

- Address: 127.0.0.1
- Port: 6653

The controller must be running and listening at the configured address and port.

## 7. Planned Connectivity Tests

The topology should be tested using Mininet commands such as:

```text
nodes
pingall
```

The nodes command lists the available network nodes.

The pingall command tests connectivity between hosts.

The results must be recorded after the topology has been launched with a compatible controller.

## 8. Running the Topology

After verifying the required Mininet, Open vSwitch, and controller setup, the intended launch command is:

```bash
cd ~/network-monitoring-system
sudo python3 topology.py
```

This command must be tested in the actual environment before it is used in the final demonstration.

## 9. Verification Status

The topology file has been created, but successful connectivity and forwarding behavior must be confirmed by testing.

The final documentation should include genuine screenshots of:

- The running Mininet topology.
- The output of the nodes command.
- The output of pingall.
- Any additional path or forwarding tests.

## 10. Integration Requirements

The topology must use a compatible SDN controller.

Telemetry agents running inside Mininet hosts also require a server address reachable from those hosts. The localhost address inside a Mininet host is not the same as the Ubuntu host's localhost address.
