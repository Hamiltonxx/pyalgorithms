# To avoid processing a node more than once, we use a boolean visited array.
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.res = []
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def dfs(self,v,visited):
        visited[v] = True 
        # print(v, end=" ")
        self.res.append(v)
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs(i,visited)

if __name__ == "__main__":
    g = Graph()
    g.addEdge(0,1)
    g.addEdge(0,2)
    g.addEdge(1,2)
    g.addEdge(2,0)
    g.addEdge(2,3)
    g.addEdge(3,3)

    visited = [False] * len(g.graph)
    g.dfs(2,visited)
    print(*g.res)