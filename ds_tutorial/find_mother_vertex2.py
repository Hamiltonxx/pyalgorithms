from collections import defaultdict

def dfs(v, visited):
    visited[v] = True 
    for u in graph[v]:  # global variable graph
        if not visited[u]:
            dfs(u, visited)

def findMother():
    visited = [False] * n # global variable n
    v = 0   # Last finished vertex / Mother vertex
    for i in range(n):
        if not visited[i]:
            dfs(i,visited)
            v = i 
    visited = [False] * n 
    dfs(v,visited)
    if not all(visited):
        return -1
    return v


if __name__ == '__main__':
    n,m = map(int, input().split())
    graph = defaultdict(list)
    # init graph
    for _ in range(m):
        u,v = map(int, input().split())
        graph[u].append(v)

    print(f"Mother Vertex: {findMother()}")
    

