# **Mininet Network Topologies**

## Router

![Network Topology 1](/images/topology_1.png)

**Commands:**

`python linuxrouter.py`

## Controller

![Network Topology 2](/images/topology_2.png)

**Commands:**

**Note: Assuming network_controller.py in ~/pox/pox/misc/**

`./pox.py log.level --DEBUG misc.network_controller`

`sudo mn --custom <path to network.py>network.py --controller remote`
