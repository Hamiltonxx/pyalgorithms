
def dfs(u,v,visited=[]):
    visited.append(u)
    for w in graph[u]:
        if w==v:
            return visited
        elif w not in visited:
            dfs(w,v,visited)
            