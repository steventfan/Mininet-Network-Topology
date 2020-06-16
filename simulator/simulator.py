import matplotlib.pyplot as plt
import random

def p2p(clusters, nodes, seeders, blackouts):
    peers = clusters * nodes
    
    if seeders > peers or blackouts > clusters:
        return 0
    
    network = [[0 for _ in range(nodes)] for _ in range(clusters)]
    
    samples = random.sample(range(peers), seeders)
    for sample in samples:
        for cluster in range(clusters):
            if sample < nodes:
                network[cluster][sample] = 1
                break
            sample -= nodes
    
    samples = random.sample(range(clusters), blackouts)
    cut = {key: None for key in samples}
    success = 0
    count = 0
    found = False
    for cluster in range(clusters):
        if cluster in cut:
            if 1 in network[cluster]:
                success += nodes
        else:
            if found:
                success += nodes
            else:
                if 1 in network[cluster]:
                    found = True
                    success += nodes + count
                else:
                    count += nodes
                    
    return success / peers
    
def server(clusters, nodes, seeders, blackouts):
    peers = clusters * nodes
    
    if seeders > peers or blackouts > clusters:
        return 0
    
    network = [[0 for _ in range(nodes)] for _ in range(clusters)]
    
    samples = random.sample(range(peers), seeders)
    for sample in samples:
        for cluster in range(clusters):
            if sample < nodes:
                network[cluster][sample] = 1
                break
            sample -= nodes
    
    samples = random.sample(range(clusters), blackouts)
    cut = {key: None for key in samples}
    success = 0
    for cluster in range(clusters):
        if cluster in cut:
            success += network[cluster].count(1)
        else:
            success += nodes
    
    return success / peers

clusters = 10
nodes = 5
seeders = clusters * nodes
blackouts = 3
iterations = 100

p2pReceive1 = []
serverReceive1 = []
for seeder in range(1, seeders + 1):
    p2pReceive = 0
    serverReceive = 0
    for _ in range(iterations):
        p2pReceive += p2p(clusters, nodes, seeder, blackouts)
        serverReceive += server(clusters, nodes, seeder, blackouts)
    p2pReceive /= iterations
    serverReceive /= iterations
    
    p2pReceive1.append(p2pReceive)
    serverReceive1.append(serverReceive)
    
iterationVariables = [i for i in range(1, seeders + 1)]
plt.plot(iterationVariables, p2pReceive1, color = 'red', label = 'p2p')
plt.plot(iterationVariables, serverReceive1, color = 'blue', label = 'server')
plt.title('Received vs Seeders')
plt.xlabel('Seeders')
plt.ylabel('Received')
plt.legend()
plt.show()

clusters = 10
nodes = 5
seeders = 3
blackouts = clusters
iterations = 100

p2pReceive2 = []
serverReceive2 = []
for blackout in range(1, blackouts + 1):
    p2pReceive = 0
    serverReceive = 0
    for _ in range(iterations):
        p2pReceive += p2p(clusters, nodes, seeders, blackout)
        serverReceive += server(clusters, nodes, seeders, blackout)
    p2pReceive /= iterations
    serverReceive /= iterations
    
    p2pReceive2.append(p2pReceive)
    serverReceive2.append(serverReceive)
    
iterationVariables = [i for i in range(1, blackouts + 1)]
plt.plot(iterationVariables, p2pReceive2, color = 'red', label = 'p2p')
plt.plot(iterationVariables, serverReceive2, color = 'blue', label = 'server')
plt.title('Received vs Blackouts')
plt.xlabel('Blackouts')
plt.ylabel('Received')
plt.legend()
plt.show()

clusters = 50
nodes = 5
seeders = 3
blackouts = 3
iterations = 100

p2pReceive3 = []
serverReceive3 = []
for cluster in range(1, clusters + 1):
    p2pReceive = 0
    serverReceive = 0
    for _ in range(iterations):
        p2pReceive += p2p(cluster, nodes, seeders, blackouts)
        serverReceive += server(cluster, nodes, seeders, blackouts)
    p2pReceive /= iterations
    serverReceive /= iterations
    
    p2pReceive3.append(p2pReceive)
    serverReceive3.append(serverReceive)
    
iterationVariables = [i for i in range(1, clusters + 1)]
plt.plot(iterationVariables, p2pReceive3, color = 'red', label = 'p2p')
plt.plot(iterationVariables, serverReceive3, color = 'blue', label = 'server')
plt.title('Received vs Clusters')
plt.xlabel('Clusters')
plt.ylabel('Received Transfers')
plt.legend()
plt.show()
