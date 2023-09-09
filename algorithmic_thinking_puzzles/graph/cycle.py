from collections import defaultdict, deque
# defaultdict potentially insert new keys, 不要在递归里使用defaultdict
from functools import lru_cache

# 有向图测环不能用并查集
# DFS
def cyclic(g):
    visited = set()
    @lru_cache(None)
    def dfs(v):
        visited.add(v)
        for u in g.get(v, []):
            if u in visited or dfs(u):
                return True
        visited.remove(v)
        return False
    return any(dfs(v) for v in g)

# BFS (Toplogical Sort)
def cyclic(g, V):
    indeg = [0] * V 
    for v in g:
        for u in g[v]:
            indeg[u] += 1
    q = deque()
    for v in range(V): # 注意这里和v in g的区别
        if indeg[v] == 0:
            q.append(v)
    cnt = 0
    while q:
        v = q.popleft()
        cnt += 1
        for u in g.get(v,[]):
            indeg[u] -= 1
            if indeg[u] == 0:
                q.append(u)
    return cnt != V

graph = {'A':['B','C'], 'B':['D'], 'C':['D'], 'D':['A']}
# d = defaultdict(list, graph)
# print(has_cycle(d))
print(cyclic(graph))

# 无向图测环
# If you know it is connected, then simply it is a tree, |E| = |V| - 1

    
        