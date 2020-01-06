from collections import defaultdict 

class Graph:
    def __init__(self,V):
        self.graph = defaultdict(list) 
        self.V = V

    def addEdge(self,u,v):
        self.graph[u].append(v) 

    def isCyclic(self):
        visited = [False] * self.V
        recStack = [False] * self.V
        def isCyclicUtil(s,visited,recStack):
            visited[s] = True 
            recStack[s] = True 
            for j in self.graph[s]:
                if not visited[j]:
                    if isCyclicUtil(j,visited,recStack):
                        return True 
                if recStack[j]:
                    return True 
            recStack[s] = False 
            return False 
            
        for i in range(self.V):
            if not visited[i]:
                if isCyclicUtil(i,visited,recStack):
                    return True 
        return False 

if __name__ == "__main__":
    g = Graph(4)
    g.addEdge(1,0)
    g.addEdge(0,2)
    g.addEdge(2,0)
    g.addEdge(0,3)
    g.addEdge(3,4)

    if g.isCyclic():
        print("Graph contains cycle")
    else:
        print("Graph does not contain cycle")

    g1 = Graph(3)
    g1.addEdge(0,1)
    g1.addEdge(1,2)
    if g1.isCyclic():
        print("Graph contains cycle")
    else:
        print("Graph does not contain cycle")
