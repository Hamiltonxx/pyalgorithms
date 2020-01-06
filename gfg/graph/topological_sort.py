from collections import defaultdict, deque

class Graph:
    def __init__(self, V):
        self.graph = defaultdict(list)
        self.V = V 

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def topologicalSort(self):
        visited = [False] * self.V 
        dq = deque()

        def topologicalSortUtil(v):
            visited[v] = True 
            for i in self.graph[v]:
                if not visited[i]:
                    topologicalSortUtil(i)
            dq.appendleft(v)

        for i in range(self.V):
            if not visited[i]:
                topologicalSortUtil(i)
        print(*dq)

if __name__ == '__main__':
    g = Graph(6)
    g.addEdge(5,2)
    g.addEdge(5,0)
    g.addEdge(4,0)
    g.addEdge(4,1)
    g.addEdge(2,3)
    g.addEdge(3,1)

    g.topologicalSort()