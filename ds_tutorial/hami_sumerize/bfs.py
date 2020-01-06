from collections import deque 

def bfs(graph, start):
    visited, Q = set(start), deque([start])
    while Q:
        v = Q.popleft()
        for u in graph[v]:
            if u not in visited:
                visited.add(u)
                Q.append(u)
    return visited