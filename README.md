# Mininet Network Topologies

## Router

![Router Topology](/images/topology_1.png)

### Commands

`python linuxrouter.py`

## Controller

![Controller Topology](/images/topology_2.png)

### Commands

**Note: Assuming network_controller.py in ~/pox/pox/misc/**

`./pox.py log.level --DEBUG misc.network_controller`

`sudo mn --custom <path to network.py>network.py --controller remote`

## Simulator

~[Simulator Topology](/images/topology_3.png)

The simulator simulates the robustness of client-server models and P2P models in an extended star network topology. The center router is connected to the Internet. The model constructs an extended star network topology with *c* clusters with *h* hosts per cluster, creating a total of *c* times *h* hosts in the network. The network is initialized with *s* seeders and with *b* blackouts created between clusters and the central router. The simulator runs *i* iterations per point, selecting random hosts and links to be seeders or blacked out respectively. The number of each variable is initialized in the source code. An average fraction of hosts in a network that would receive the simulated file transfers depending on the model is returned. Three graphs show the relationship between this fraction and the variables: seeders, blackouts, and clusters respectively.

### Commands

`python simulator.py`
