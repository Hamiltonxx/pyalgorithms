# 用DFS来检测图是否是二分图
def check_bipartite_dfs(g):
    visited = [False] * len(g)
    color = [-1] * len(g)