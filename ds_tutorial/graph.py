#         A 
#        / \
#       /   \
#      B --- C
#       \   /|
#        \ / | 
#         E  F
graph = dict()
graph['A'] = ['B','C']
graph['B'] = ['E','C','A']
graph['C'] = ['A','B','E','F']
graph['E'] = ['B','C']
graph['F'] = ['C']

matrix_elements = sorted(graph.keys())
cols = rows = len(matrix_elements)
adjacency_matrix = [[0 for x in range(rows)] for y in range(rols)]
edges_list = []

for key in matrix_elements:
    for neighbor in graph[key]:
        edges_list.append((key,neighbor))

