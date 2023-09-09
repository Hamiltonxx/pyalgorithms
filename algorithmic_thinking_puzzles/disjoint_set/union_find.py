# n node graph
n = 10
parent = list(range(n))

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    aroot, broot = find(a), find(b)
    if aroot != broot:
        parent[aroot] = broot

