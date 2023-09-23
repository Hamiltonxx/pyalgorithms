# n node graph
n = 10
# parent = list(range(n))

# def find(a):
#     if parent[a] != a:
#         parent[a] = find(parent[a])
#     return parent[a]

# def union(a,b):
#     aroot, broot = find(a), find(b)
#     if aroot != broot:
#         parent[aroot] = broot


p = list(range(n))
size = [1] * n 

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]
def union(x,y): # by size
    xroot,yroot = find(x),find(y)
    if xroot != yroot:
        p[xroot] = yroot
        size[yroot] += size[xroot]


