class Solution:
    def allPaths(self, graph):
        self.paths = []
        dest = len(graph)-1
        def dfs(v, path):
            if v == dest:
                self.paths.append(path+[v])
            for u in graph[v]:
                dfs(u, path+[v])
        dfs(0, [])
        return self.paths

# class Solution:
#     def allPaths(self, graph):
#         self.paths = []
#         dest = len(graph) - 1
#         def dfs(v, path):
#             for u in graph[v]:
#                 if u == dest:
#                     self.paths.append(path+[u])
#                 dfs(u, path+[v])  
#         dfs(0, [0])
#         return self.paths 
        
def allPaths(graph):
    res = []
    stack = [[0]]   
    while stack:
        path = stack.pop()
        if path[-1] == len(graph) - 1:
            res.append(path)
        else:
            for u in graph[path[-1]]:
                stack.append(path+[u])
    return res

