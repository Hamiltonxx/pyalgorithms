# Adjacency Matrix
class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[False] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, i, j):
        self.adj_matrix[i][j] = True 
        self.adj_matrix[j][i] = True 

    def remove_edge(self, i, j):
        self.adj_matrix[i][j] = False 
        self.adj_matrix[j][i] = False 

# Adjacency List
# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'C', 'D'],
#     'C': ['A', 'B', 'D'],
#     'D': ['B', 'C']
# }
class Graph2:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        self.adj_list[vertex] = []

    def add_edge(self, source, destination):
        if source in self.adj_list:
            self.adj_list[source].append(destination)
        else:
            self.adj_list[source] = [destination]

        if destination not in self.adj_list:
            self.adj_list[destination] = []

# Create an instance of the graph
graph = Graph2()

# Add vertices
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')

# Add edges
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'D')


def dfs(graph, start_vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(start_vertex)
    print(start_vertex)

    for neighbor in graph[start_vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

testgraph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}
dfs(testgraph, 'A')

from collections import deque 

def bfs(graph, start_vertex):
    visited = set()
    queue = deque([start_vertex])
    visited.add(start_vertex)

    while queue:
        vertex = queue.popleft()
        print(vertex)
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

bfs(testgraph, 'A')