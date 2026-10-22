#!/usr/bin/env python3

from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel


class MonitoringTopology(Topo):

    def build(self):

        # Create four switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')

        # Create four hosts
        h1 = self.addHost('h1', ip='10.0.0.1/24')
        h2 = self.addHost('h2', ip='10.0.0.2/24')
        h3 = self.addHost('h3', ip='10.0.0.3/24')
        h4 = self.addHost('h4', ip='10.0.0.4/24')

        # Connect hosts to switches
        self.addLink(h1, s1)
        self.addLink(h2, s2)
        self.addLink(h3, s3)
        self.addLink(h4, s4)

        # Connect switches to create two paths
        self.addLink(s1, s2)
        self.addLink(s2, s4)
        self.addLink(s1, s3)
        self.addLink(s3, s4)


def run():
    topo = MonitoringTopology()

    net = Mininet(
        topo=topo,
        controller=None,
        autoSetMacs=True
    )

    # Connect to a remote SDN controller
    net.addController(
        'c0',
        controller=RemoteController,
        ip='127.0.0.1',
        port=6653
    )

    net.start()

    print("\nNetwork Monitoring Topology Started!")
    print("Hosts: h1, h2, h3, h4")
    print("Switches: s1, s2, s3, s4")
    print("Two paths exist between h1 and h4.")
    print("\nType 'pingall' to test connectivity.")
    print("Type 'nodes' to list network nodes.")
    print("Type 'exit' to stop the topology.\n")

    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    run()
