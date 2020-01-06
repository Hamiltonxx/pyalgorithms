import heapq 
import math

def calc_distances(graph, starting_vertex):
    distances = {vertex:math.inf for vertex in graph}
    distances[starting_vertex] = 0

    pq = [(0,starting_vertex)]
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue 

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight 
            if distance < distances[neighbor]:
                distances[neighbor] = distance 
                heapq.heappush(pq, (distance,neighbor))

    return distances

example_graph = {
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}

print(calc_distances(example_graph, 'X'))
# {'U': 1, 'V': 2, 'W': 2, 'X': 0, 'Y': 1, 'Z': 2}