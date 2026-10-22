#!/usr/bin/env python3
import time
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSSwitch
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel, info


class P2Topology(Topo):
    def build(self):
        # Four hosts
        h1 = self.addHost('h1', ip='10.0.0.1/24')
        h2 = self.addHost('h2', ip='10.0.0.2/24')
        h3 = self.addHost('h3', ip='10.0.0.3/24')
        h4 = self.addHost('h4', ip='10.0.0.4/24')

        # Four OVS switches, standalone mode with STP to break the loop
        s1 = self.addSwitch('s1', cls=OVSSwitch, failMode='standalone', stp=True)
        s2 = self.addSwitch('s2', cls=OVSSwitch, failMode='standalone', stp=True)
        s3 = self.addSwitch('s3', cls=OVSSwitch, failMode='standalone', stp=True)
        s4 = self.addSwitch('s4', cls=OVSSwitch, failMode='standalone', stp=True)

        # Host links
        self.addLink(h1, s1, bw=10)
        self.addLink(h2, s1, bw=10)
        self.addLink(h3, s4, bw=10)
        self.addLink(h4, s4, bw=10)

        # Path A: s1 -> s2 -> s4
        self.addLink(s1, s2, bw=10)
        self.addLink(s2, s4, bw=10)

        # Path B: s1 -> s3 -> s4
        self.addLink(s1, s3, bw=10)
        self.addLink(s3, s4, bw=10)


def run():
    net = Mininet(topo=P2Topology(), link=TCLink,
                  controller=None, autoSetMacs=True)
    net.start()
    for h in net.hosts:
        h.cmd('ethtool -K %s-eth0 tso off gso off gro off' % h.name)

    info('*** Waiting 35 seconds for STP to converge\n')
    time.sleep(35)

    info('\nP2 topology started.\n')
    info('Hosts: h1 10.0.0.1, h2 10.0.0.2, h3 10.0.0.3, h4 10.0.0.4\n')
    info('Switches: s1, s2, s3, s4 (OVS standalone + STP)\n')
    info('Links: 8, all 10 Mbit/s\n\n')

    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    run()
