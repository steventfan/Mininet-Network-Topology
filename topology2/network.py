from mininet.topo import Topo

class MyTopo(Topo):

    def build(self):

        h1, h2, h3, h4, h5 = [self.addHost(h, ip = ip) for h, ip in (('h1', '10.0.0.1/16'), ('h2', '10.0.0.2/16'), ('h3', '10.0.0.3/16'), ('h4', '10.0.1.2/16'), ('h5', '10.0.1.3/16'))]

        s1, s2, s3 = [self.addSwitch(s) for s in ('s1', 's2', 's3')]

        for l1, l2, name in [(h1, s1, 'h1-s1'), (h2, s1, 'h2-s1'), (h3, s1, 'h3-s1'), (h4, s3, 'h4-s3'), (h5, s3, 'h5-s3'), (s1, s2, 's1-s2'), (s2, s3, 's2-s3')]:
            self.addLink(l1, l2, intfName2 = name)

topos = {'mytopo': (lambda: MyTopo())}
