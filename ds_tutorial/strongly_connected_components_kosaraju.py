# 如果一个有向图的所有点之间都有路径，那么它是强连通图
# 一个有向图的强连通分量(SCC)是最大强连通子图
def dfs(u):
    global g,r,scc,component,visit,stack 
    if visit[u]: return 
    visit[u] = True 
    for v in g[u]:
        dfs(v)
    stack.append(u)

def dfs2(u):
    global g,r,scc,component,visit,stack 
    if visit[u]: return 
    visit[u] = True 
    component.append(u)
    for v in r[u]:
        dfs2(v)

def kosaraju():
    global g,r,scc,component,visit,stack 
    for i in range(n):
        dfs(i)
    visit = [False]*n 
    for i in stack[::-1]:
        if visit[i]: continue
        component = []
        dfs2(i)
        scc.append(component)
    return scc 

if __name__ == "__main__":
    n,m = map(int,input().split())
    g = [[] for i in range(n)] #graph
    r = [[] for i in range(n)] #reversed graph
    for i in range(m):
        u,v = map(int,input().split())
        g[u].append(v)
        r[v].append(u)

    stack = []
    visit = [False]*n
    scc = []
    component = []
    print(kosaraju())

