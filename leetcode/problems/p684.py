def findRedundantConnection(edges):
    n = len(edges)
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
        if find(u-1) == find(v-1):
            return [u,v]
        union(u-1,v-1)
        
edges = [[9,10],[5,8],[2,6],[1,5],[3,8],[4,9],[8,10],[4,10],[6,8],[7,9]]
print(findRedundantConnection(edges))

