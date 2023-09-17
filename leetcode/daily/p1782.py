from collections import defaultdict
def countPairs(n, edges, queries):
    deg = [0] * (n+1)
    ctr = defaultdict(int)
    for u,v in edges:
        deg[u] += 1
        deg[v] += 1
        ctr[min(u,v),max(u,v)] += 1
    sdeg = sorted(deg)

    ans = []
    for q in queries:
        l, r = 1, n
        a = 0
        while l < r:
            if sdeg[l] + sdeg[r] > q:
                a += r - l
                r -= 1 
            else:
                l += 1
        for (u,v),c in ctr.items():
            if q < deg[u] + deg[v] <= q+c:
                a -= 1
        ans.append(a)

    return ans

n = 4
edges = [[1,2],[2,4],[1,3],[2,3],[2,1]]
queries = [2,3]
print(countPairs(n, edges, queries))