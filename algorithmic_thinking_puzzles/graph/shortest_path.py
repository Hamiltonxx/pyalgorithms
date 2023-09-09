graph = {
    'A': {'B':4, 'C':2},
    'B': {'A':4, 'C':1, 'D':5},
    'C': {'A':2, 'B':1, 'D':8},
    'D': {'B':5, 'C':8}
}

import heapq 

# def dijkstra(graph, start):
#     distances = {vertex: float('inf') for vertex in graph}
#     distances[start] = 0

#     pq = [(0, start)]
#     while pq:
#         current_distance, current_vertex = heapq.heappop(pq)

#         if current_distance > distances[current_vertex]:
#             continue 

#         for neighbor, weight in graph[current_vertex].items():
#             distance = current_distance + weight
#             if distance < distances[neighbor]:
#                 distances[neighbor] = distance 
#                 heapq.heappush(pq, (distance, neighbor))

#     return distances 

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




