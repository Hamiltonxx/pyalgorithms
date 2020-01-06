import heapq 

# Shortest path between vertexes
def dijkstra(graph, start, end):
    heap = [(0,start)]
    visited = set()
    while heap:
        (cost,u) = heapq.heappop(heap)
        if u in visited:
            continue 
        visited.add(u)
        if u == end:
            return cost 
        for v,c in graph[u]:
            if v in visited:
                continue
            next = cost + c 
            heapq.heappush(heap, (next,v))
    return -1

## Geeksforgeeks https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/  ##
Geeks = {
    0: [(1,4),(7,8)],
    1: [(0,4),(2,8),(7,11)],
    2: [(1,8),(3,7),(5,4),(8,2)],
    3: [(2,7),(4,9),(5,14)],
    4: [(3,9),(5,10)],
    5: [(2,4),(3,14),(4,10),(6,2)],
    6: [(5,2),(7,1),(8,6)],
    7: [(0,8),(1,11),(6,1),(8,7)],
    8: [(2,2),(6,6),(7,8)]
}

shortDistance_geeks = dijkstra(Geeks, 0, 4)
print(shortDistance_geeks)


# G = {
#     "A": [("B",2),("C",5)],
#     "B": [("A",2),("D",3),("E",1),("F",1)],
#     "C": [("A",5),("F",3)],
#     "D": [("B",3)],
#     "E": [("B",4),("F",3)],
#     "F": [("C",3),("E",3)],
# }

# r"""
# Layout of G2:
# E -- 1 --> B -- 1 --> C -- 1 --> D -- 1 --> F
#  \                                         /\
#   \                                        ||
#     ----------------- 3 --------------------
# """
# G2 = {
#     "B": [["C", 1]],
#     "C": [["D", 1]],
#     "D": [["F", 1]],
#     "E": [["B", 1], ["F", 3]],
#     "F": [],
# }

# r"""
# Layout of G3:
# E -- 1 --> B -- 1 --> C -- 1 --> D -- 1 --> F
#  \                                         /\
#   \                                        ||
#     -------- 2 ---------> G ------- 1 ------
# """
# G3 = {
#     "B": [["C", 1]],
#     "C": [["D", 1]],
#     "D": [["F", 1]],
#     "E": [["B", 1], ["G", 2]],
#     "F": [],
#     "G": [["F", 1]],
# }

# shortDistance = dijkstra(G, "E", "C")
# print(shortDistance)  # E -- 3 --> F -- 3 --> C == 6

# shortDistance = dijkstra(G2, "E", "F")
# print(shortDistance)  # E -- 3 --> F == 3

# shortDistance = dijkstra(G3, "E", "F")
# print(shortDistance)  # E -- 2 --> G -- 1 --> F == 3