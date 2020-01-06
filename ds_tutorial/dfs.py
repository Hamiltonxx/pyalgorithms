def dfs_rec(graph, v, visited=[]):
    visited.append(v)
    for u in graph[v]:
        if u not in visited:
            visited = dfs_rec(graph, u, visited)
    return visited 

graph = {1:[2,3],
         2:[1,4,5,6],
         3:[1,4],
         4:[2,3,5],
         5:[2,4,6],
         6:[2,5]}
#                1
#               / \
#          6 - 2   3
#           \ / \ /
#            5 - 4
print(dfs_rec(graph,1))


def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        v = stack.pop()
        if v in visited:
            continue
        visited.add(v)
        for w in graph[v]:
            if w not in visited:
                stack.append(w)
    return visited

# G = {'A': ['B', 'C'],
#      'B': ['A', 'D', 'E'],
#      'C': ['A', 'F'],
#      'D': ['B'],
#      'E': ['B', 'F'],
#      'F': ['C', 'E']}

# print(dfs(G, 'A'))
print(dfs(graph,6))