from collections import defaultdict 

class Graph:
    def __init__(self, V):
        self.graph = defaultdict(list)
        self.V = V

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def bfs(self, s):
        visited = [False] * self.V
        queue = []
        queue.append(s)
        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            visited[s] = True 
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)

    def dfs(self, s):
        visited = [False] * self.V

        def dfsUtil(start):
            visited[start] = True 
            print(start, end=" ")
            for i in self.graph[start]:
                if not visited[i]:
                    dfsUtil(i)
        dfsUtil(s)

if __name__ == '__main__':
    g = Graph()
    g.addEdge(0,1)
    g.addEdge(0,2)
    g.addEdge(1,2)
    g.addEdge(2,0)
    g.addEdge(2,3)
    g.addEdge(3,3)

    print("BFS from vertex 2: ")
    g.bfs(2)
    #2 0 3 1
    print("DFS from vertex 2: ")
    g.dfs(2)
    #2 0 1 3