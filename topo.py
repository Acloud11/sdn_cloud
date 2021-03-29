
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class Sdn_topo:

    def build(self, n = 2):
        switch = self.addSwitch('s1')
        for i in range(n):
            host = self.addHost('h{}'.format(n + 1))
            self.addLink(host, switch)

def start():
    "Create and test a simple network"
    topo = Sdn_topo(n=4)
    net = Mininet(topo)
    net.start()
    print("Dumping host connections")
    dumpNodeConnections(net.hosts)
    print("Testing network connectivity")
    net.pingAll()
    net.stop()

if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    start()