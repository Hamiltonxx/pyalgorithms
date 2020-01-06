# A back edge is an edge that is from a node to itself(self-loop) or one of its ancestor
# in the tree produced by dfs
# To detect a back edge, we can keep track of vertices currently in recursion stack
# of function for dfs traversal. If we reach a vertex that is already in the recursion stack,
# then there is a cycle in the tree.
from collections import defaultdict 
class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def isCyclicUtil(self,v,visited,recStack):
        visited[v] = True 
        recStack[v] = True
        for neighbour in self.graph[v]:
            if not visited[neighbour]:
                if self.isCyclicUtil(neighbour,visited,recStack):
                    return True
            elif recStack[neighbour]:
                return True 
        recStack[v] = False
        return False 
    def isCyclic(self):
        visited = [False] * self.V 
        recStack = [False] * self.V 
        for node in range(self.V):
            if not visited[node]:
                if self.isCyclicUtil(node,visited,recStack):
                    return True
        return False

      #         2 <-- 5
      #         ^      \
      #         |       \
      #         |        >
      #         0  <---- 6
      #        /         |
      #       /          |
      #      <           ~
      #     1   <------  4
      #    /
      #   /
      #  < 
      # 3 

if __name__ == "__main__":
    # g = Graph(4) 
    # g.addEdge(0, 1) 
    # g.addEdge(0, 2) 
    # g.addEdge(1, 2) 
    # g.addEdge(2, 0) 
    # g.addEdge(2, 3) 
    # g.addEdge(3, 3) 
    g = Graph(7)
    g.addEdge(0,1)
    g.addEdge(0,2)
    g.addEdge(1,3)
    g.addEdge(4,1)
    g.addEdge(5,2)
    g.addEdge(5,6)
    g.addEdge(6,0)
    g.addEdge(6,4)

    if g.isCyclic():
        print("Graph has cycle!")
    else:
        print("There is no cycle!")