from collections import defaultdict

def dfs(v, visited=[]):
    visited.append(v)
    for u in graph[v]: #global variable graph
        if u not in visited:
            visited = dfs(u, visited)
    return visited

def findMother():
    for i in range(n): #global variable n
        visited = []
        visited = dfs(i,visited)
        if len(visited) == n:
            return i
    return -1

if __name__ == '__main__':
    n,m = map(int, input().split())
    graph = defaultdict(list)

    for _ in range(m):
        u,v = map(int, input().split())
        graph[u].append(v)

    print(f"Mother Vertex: {findMother()}")
    # print(dfs(6))
    # for i in range(n):
    #     vis = []
    #     print(dfs(i,vis))


