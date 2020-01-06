def allPathsRec(u,w,visited,path):
    print(f"visiting.. {u}")
    visited[u] = True 
    path.append(u)
    print(f"path: {path}")
    if u == w:
        print(path)
    else:
        for v in graph[u]:
            print(f"when v is {v}..")
            if not visited[v]:
                allPathsRec(v,w,visited,path)
    tmp = path.pop()
    visited[u] = False
    print(f"poping.. {tmp} and setting.. {u} False")


from collections import defaultdict

n,m = map(int,input().split())
graph = defaultdict(list)
for _ in range(m):
    u,v = map(int, input().split())
    graph[u].append(v)
print(graph)

visited = [False] * n 
path = []
allPathsRec(5,3,visited,path)