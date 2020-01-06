from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices 
        self.graph = defaultdict(list)

    # def DFSUtil(self, v, visited):
    #     visited[v] = True 
    #     for u in self.graph[v]:
    #         if visited[u] == False:
    #             self.DFSUtil(u, visited)
    def dfs(self, v, visited):
        visited[v] = True 
        for u in self.graph[v]:
            if not visited[u]:
                self.dfs(u,visited)

    def addEdge(self, v, w):
        self.graph[v].append(w)

    def findMother(self):
        visited = [False] * self.V 
        # Last finished vertex / Mother vertex
        v = 0 
        for i in range(self.V):
            if not visited[i]:
                self.dfs(i,visited)
                v = i 

        visited = [False] * self.V 
        self.dfs(v,visited)
        if not all(visited):
            return -1
        else:
            return v 

g = Graph(7)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,3)
g.addEdge(1,4)
g.addEdge(5,2)
g.addEdge(5,6)
g.addEdge(6,0)

print("A mother vertex is {}".format(g.findMother()) )