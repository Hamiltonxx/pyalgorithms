from collections import defaultdict, deque
from math import inf 

class Graph:
    def __init__(self, V):
        self.graph = defaultdict(list)
        self.V = V 

    def addEdge(self,u,v,w):
        self.graph[u].append([v,w])

    def topologicalSort(self):
        visited = [False] * self.V 
        dq = deque()

        def topologicalSortUtil(u):
            visited[u] = True 
            for v in self.graph[u]:
                if not visited[v[0]]:
                    topologicalSortUtil(v[0])
            dq.appendleft(u)

        for i in range(self.V):
            if not visited[i]:
                topologicalSortUtil(i)
        return dq

    def longestPath(self):
        dist = [-inf] * self.V
        dist[1] = 0  # 假设1为起点
        dq = self.topologicalSort()
        for u in dq:
            for v in self.graph[u]:
                if dist[v[0]] < dist[u] + v[1]:
                    dist[v[0]] = dist[u] + v[1]
        return dist

if __name__ == '__main__':
    g = Graph(6)
    g.addEdge(0, 1, 5)  
    g.addEdge(0, 2, 3)  
    g.addEdge(1, 3, 6)  
    g.addEdge(1, 2, 2)  
    g.addEdge(2, 4, 4)  
    g.addEdge(2, 5, 2)  
    g.addEdge(2, 3, 7)  
    g.addEdge(3, 5, 1)  
    g.addEdge(3, 4, -1) 
    g.addEdge(4, 5, -2)

    print(g.longestPath())
    # [-inf, 0, 2, 9, 8, 10]

