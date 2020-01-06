from collections import defaultdict

def dfs(v, w):
    # visited[v] = True 
    # res = False
    global res
    for u in graph[v]:
        if u == w:
            res = True
        else:
            dfs(u,w)
    # return res

# def isReachable(u,v):
#     visited = [False] * n 
#     dfs(u, visited)

if __name__ == '__main__':
    n,m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u,v = map(int, input().split())
        graph[u].append(v)
    print(graph)
    # visited = [False] * 7
    # end = 3
    # print(dfs(5,visited))

    res = False
    dfs(0,4)
    print(res)