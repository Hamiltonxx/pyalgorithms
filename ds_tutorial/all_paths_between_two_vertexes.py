from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def allPathRec(self,u,w,visited,path):
        visited[u] = True 
        path.append(u)
        if u == w:
            print path 
        else:
            for v in self.graph[u]:
                if not visited[v]:
                    self.allPathRec(v,w,visited,path)

        path.pop()
        visited[u] = False 

    def printAllPaths(self, s, d):
        visited = [False] * self.V 
        path = []
        self.allPathRec(s,d,visited,path)

g = Graph(4) 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(0, 3) 
g.addEdge(2, 0) 
g.addEdge(2, 1) 
g.addEdge(1, 3) 
s,d = 2,3
print(f"All paths from {s} to {d} :")
g.printAllPaths(s,d)