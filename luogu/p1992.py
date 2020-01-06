from collections import defaultdict

def isCyclicUtil(v,visited,recStack):
    visited[v] = True 
    recStack[v] = True 
    for neighbour in graph[v]:
        if not visited[neighbour]:
            if isCyclicUtil(neighbour,visited,recStack):
                return True 
        if recStack[neighbour]:
            return True 
    recStack[v] = False 
    return False 

def isCyclic():
    visited = [False] * n 
    recStack = [False] * n 
    for i in range(n):
        if not visited[i]:
            if isCyclicUtil(i,visited,recStack):
                return True 
    return False 

n,m,k = map(int,input().split())
graph = defaultdict(list)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a-1].append(b-1)

if isCyclic():
    print("No")
    print(k**2)
else:
    print("Yes")
    print((2**k)%9997)