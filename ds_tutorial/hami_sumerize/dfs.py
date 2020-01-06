def dfs_rec(graph, v, visited=[]):
    visited.append(v)
    for u in graph[v]:
        if u not in visited:
            visited = dfs_rec(graph,u,visited)
    return visited

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        v = stack.pop()
        if v in visited:
            continue
        visited.add(v)
        for u in graph[v]:
            if u not in visited:
                stack.append(u)
    return visited