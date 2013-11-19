from sys import maxsize
from heapq import heappush, heappop

#
# Dijkstra's all-pair shortest paths algorithm, in python
#

class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
        self.weights = []
        self.visited = False
        self.distance = maxsize


    def addEdge(self, node, weight):
        self.neighbors.append(node)
        self.weights.append(weight)

        node.neighbors.append(self)
        node.weights.append(weight)

    def __lt__(self, other):
        return self.distance < other.distance


def shortest_paths(src, nodes):
    # distance from src to node
    
    pq = []
    src.distance = 0
    heappush(pq, src)

    while(len(pq) > 0):
        current = heappop(pq)
        print('processing ' + current.name + ' with distance ' + str(current.distance))
        for child, weight in zip(current.neighbors, current.weights):
            if not child.visited:
                d = current.distance + weight
                if d < child.distance:
                    # add to pq
                    # this can cause extra work if the node is already in PQ
                    # and needs its key decreased.
                    heappush(pq, child)
                    child.distance = d

        current.visited = True

    return [(n.name, n.distance) for n in nodes]


n1 = Node('1') 
n2 = Node('2') 
n3 = Node('3') 
n4 = Node('4') 
n5 = Node('5') 
n6 = Node('6') 

n1.addEdge(n2, 7)
n1.addEdge(n3, 9)
n1.addEdge(n6, 14)
n2.addEdge(n3, 10)
n2.addEdge(n4, 15)
n3.addEdge(n6, 2)
n3.addEdge(n4, 11)
n4.addEdge(n5, 6)
n5.addEdge(n6, 9)

nodes = [n1, n2, n3, n4, n5, n6]

print(str(shortest_paths(n1, [n1, n2, n3, n4, n5, n6])))
