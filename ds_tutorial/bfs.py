from collections import deque
def bfs(graph, start):
    visited,Q = set(start), deque([start])
    while Q:
        u = Q.popleft()
        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                Q.append(v)
    return visited 


G = {'A': ['B', 'C'],
     'B': ['A', 'D', 'E'],
     'C': ['A', 'F'],
     'D': ['B'],
     'E': ['B', 'F'],
     'F': ['C', 'E']}
print(bfs(G,'A'))
