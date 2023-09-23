def validPath(n, edges, source, destination):
    parent = list(range(n))
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    def union(x,y):
        xroot,yroot = find(x),find(y)
        if xroot != yroot:
            parent[xroot] = yroot
    for u,v in edges:
        union(u,v)
    return find(source) == find(destination)