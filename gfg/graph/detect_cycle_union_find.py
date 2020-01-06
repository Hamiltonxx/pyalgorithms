from collections import defaultdict 

class Graph:
    def __init__(self,V):
        self.graph = defaultdict(list)
        self.V = V 

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def isCyclic(self):
        parent = [-1] * self.V 
        def findParent(v):
            if parent[v] == -1:
                return v
            else:
                return findParent(parent[v])

        for i in self.graph:
            for j in self.graph[i]:
                x = findParent(i)
                y = findParent(j)
                if x==y:
                    return True
                parent[x] = y # union

if __name__ == '__main__':
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