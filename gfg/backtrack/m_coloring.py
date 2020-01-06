class Graph():
    def __init__(self,vertices):
        self.V = vertices
        self.graph = None 

    def isSafe(self,v,color,c):
        for i in range(self.V):
            if self.graph[v][i]==1 and color[i]==c:
                return False 
        return True 

    def graphColorUtil(self,m,color,v):
        if v == self.V:
            return True 
        for c in range(1,m+1):
            if self.isSafe(v,color,c):
                color[v] = c
                if self.graphColorUtil(m,color,v+1):
                    return True 
                color[v] = 0

    def graphColoring(self,m):
        color = [0] * self.V 
        if self.graphColorUtil(m,color,0) == None:
            return False 
        return color 

#    1
#   / \
#  /   \
# 0 --- 2
#  \   /
#   \ /
#    3
# 测试代码
g = Graph(4)
g.graph = [[0,1,1,1], [1,0,1,0], [1,1,0,1], [1,0,1,0]]
m = 3
print(g.graphColoring(m))
# [1, 2, 3, 2]