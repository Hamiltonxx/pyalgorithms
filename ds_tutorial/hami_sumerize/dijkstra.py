from collections import heapq 

def dijkstra(graph, start, end):
    visited, heap = set(), [(0,start)]
    while heap:
        (cost,v) = heapq.heappop(heap)
        if v in visited:
            continue
        visited.add(v)
        if v == end:
            return cost 
        for u,c in graph[v]:
            if u in visited:
                continue 
            next = cost + c
            heapq.heappush(heap,(next,u))
    return -1
