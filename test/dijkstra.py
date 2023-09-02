import heapq 

graph = {
    'A': {'B':4, 'C':2},
    'B': {'A':4, 'C':1, 'D':5},
    'C': {'A':2, 'B':1, 'D':8},
    'D': {'B':5, 'C':8}
}

def dijkstra(graph, start):
    d = {v:float('inf') for v in graph}
    d[start] = 0
    q = [(0,start)]
    while q:
        curd,curv = heapq.heappop(q)
        if curd > d[curv]:
            continue
        for u,w in graph[curv].items():
            if curd + w < d[u]:
                d[u] = curd + w 
                heapq.heappush(q,(d[u],u))
    return d

print(dijkstra(graph, 'A'))