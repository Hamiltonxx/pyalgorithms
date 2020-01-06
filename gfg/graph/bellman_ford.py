from collections import defaultdict 
import math 

class Graph:
    def __init__(self, V):
        self.V = V 
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u,v,w])

    def bellmanford(self, src):
        dist = [math.inf] * self.V 
        dist[src] = 0 

        # Relax all edges |V| - 1 times. A simple shortest path from src to any other vertex can have at-most |V| - 1 edges
        for i in range(self.V-1):
            for u,v,w in self.graph:
                if dist[u] != math.inf and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w 

        # Check for negative-weight cycles.
        for u,v,w in self.graph:
            if dist[u] != math.inf and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return 
        print(dist)

g = Graph(5) 
g.addEdge(0, 1, -1) 
g.addEdge(0, 2, 4) 
g.addEdge(1, 2, 3) 
g.addEdge(1, 3, 2) 
g.addEdge(1, 4, 2) 
g.addEdge(3, 2, 5) 
g.addEdge(3, 1, 1) 
g.addEdge(4, 3, -3) 
  
g.bellmanford(0)
# [0, -1, 2, -2, 1]