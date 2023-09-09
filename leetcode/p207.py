from collections import defaultdict, deque
# defaultdict potentially insert new keys
from functools import lru_cache, cache
def canFinish(numCourses, prerequisites):
    d = {}
    for u,v in prerequisites:
        if v not in d: d[v] = []
        d[v].append(u)
    
    visited = set()
    @lru_cache(None)
    def dfs(v):
        visited.add(v)
        for u in d.get(v, []):
            if u in visited or dfs(u):
                return True
        visited.remove(v)
        return False
    
    return any(dfs(v) for v in d)

# def can_finish(numCourses, prerequisites):
#     def isdag(g, root):
#         seen = set()
#         @cache 
#         def helper(node):
#             return node not in seen and (seen.add(node), all(map(helper, g[node])), seen.remove(node))[1]
#         return helper(root)
    
#     d = {}
#     for u,v in prerequisites:
#         if v not in d: d[v] = []
#         d[v].append(u)

#     return not any(isdag(d, v) for v in d)

# Toplogical Sort
def can_finish(numCourses, prerequisites):
    g = {}
    indeg = [0] * numCourses
    
    for u,v in prerequisites:
        if v not in g: g[v] = []
        g[v].append(u)
        indeg[u] += 1
    
    q = deque()
    for v in range(numCourses):
        if indeg[v] == 0:
            q.append(v)

    cnt = 0
    while q:
        v = q.popleft()
        cnt += 1
        for u in g.get(v, []):
                indeg[u] -= 1
                if indeg[u] == 0:
                    q.append(u)

    return cnt == numCourses 
        

        

# print(canFinish(4, [[1,0],[2,0],[3,1],[3,2]]))
print(can_finish(4, [[1,0],[2,0],[3,1],[3,2]]))
print(can_finish(1,[]))
print(can_finish(5, [[1,4],[2,4],[3,1],[3,2]]))
