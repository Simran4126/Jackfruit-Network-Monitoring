# P3: SDN Controller and Network Flow Monitoring

## 1. Introduction

The SDN controller component is intended to manage communication with the virtual network switches and support network traffic monitoring.

The controller will be integrated with the Mininet topology and used to demonstrate Software-Defined Networking concepts.

## 2. Objectives

- Establish communication between the controller and compatible switches.
- Support switch connection and forwarding operations.
- Work with OpenFlow-compatible switches.
- Obtain or display network flow statistics if supported by the implementation.
- Support network monitoring experiments.

## 3. Controller Framework

The exact controller framework must be documented after the implementation is received and verified.

The final documentation must identify:

- Controller framework and version.
- Required Python packages.
- Installation instructions.
- Controller source files.
- Startup command.
- OpenFlow version or configuration requirements.

## 4. Controller and Switch Communication

The current topology.py file is configured to connect to a controller at:

- Address: 127.0.0.1
- Port: 6653

The controller must listen on the configured address and port.

The controller configuration and switch configuration must be compatible.

## 5. Flow Statistics

OpenFlow-compatible switches can maintain flow-table statistics, depending on their configuration and capabilities.

The integrated controller implementation should demonstrate the statistics it actually supports.

The final demonstration should record genuine output showing available information, such as:

- Flow match fields.
- Packet counts.
- Byte counts.
- Flow-table information.

The exact fields and method of displaying the statistics depend on the selected controller and implementation.

## 6. Integration Procedure

The controller should be tested in the following order:

1. Install the required controller framework.
2. Start the controller.
3. Confirm that it is listening at the configured address and port.
4. Start the Mininet topology.
5. Confirm that the switches connect to the controller.
6. Test host connectivity.
7. Generate network traffic.
8. Display the supported flow statistics.

## 7. Verification Status

The controller source code and framework-specific instructions must be added after the implementation is received.

The controller should not be considered operational until the switch connections, forwarding behavior, and required flow-statistics demonstration have been tested.

## 8. Evidence to Collect

The final report should include screenshots showing:

- The controller starting successfully.
- Switches connecting to the controller.
- Successful connectivity tests.
- Flow statistics before or after generating traffic.
- Any additional controller output required for the demonstration.
