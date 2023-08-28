graph = {
    'A': {'B':4, 'C':2},
    'B': {'A':4, 'C':1, 'D':5},
    'C': {'A':2, 'B':1, 'D':8},
    'D': {'B':5, 'C':8}
}
# 计算A到其他各点的最短距离

import heapq 

def dijkstra(graph, start):
    d = {v: float('inf') for v in graph}
    d[start] = 0

    pq = [(0,start)]
    while pq:
        cd,cv = heapq.heappop(pq)
        if cd > d[cv]:
            continue 
        for neighbor,w in graph[cv].items():
            if cd+w < d[neighbor]:
                d[neighbor] = cd+w 
                heapq.heappush(pq, (d[neighbor],neighbor))

    return d 

print(dijkstra(graph,'A'))
print(dijkstra(graph,'A')['D'])