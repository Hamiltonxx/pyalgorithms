from collections import deque
def findOrder(numCourses, prerequisites):
    g, indeg = {}, [0]*numCourses
    for u,v in prerequisites:
        if v not in g: g[v] = []
        g[v].append(u)
        indeg[u] += 1
    
    q = deque()
    for v in range(numCourses):
        if indeg[v]==0:
            q.append(v)

    order = []
    while q:
        v = q.popleft()
        order.append(v)
        for u in g.get(v, []):
            indeg[u] -= 1
            if indeg[u] == 0:
                q.append(u)

    return order if len(order)==numCourses else []

