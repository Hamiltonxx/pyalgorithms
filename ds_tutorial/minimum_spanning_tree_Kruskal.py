# Minimum Spanning Tree
# A spanning tree of connected undirected graph is a subgraph that is a tree and connects 
# all the vertices together.
# A minimum spanning tree for a weighted,connected and undirected graph is a spanning tree
# with weight less than or equal to the weight of every other spanning tree.

# Kruskal’s Minimum Spanning Tree Algorithm
#1. Sort all the edges in non-decreasing order of their weight.
#2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it.
#3. Repeat step#2 until there are (V-1) edges in the spanning tree.
num_nodes, num_edges = list(map(int, input().split()))
edges = []

for i in range(num_edges):
    node1, node2, cost = list(map(int,input().split()))
    edges.append((i,node1,node2,cost))
     
edges.sort(key=lambda edge: edge[3])

parent = list(range(num_nodes))

def find_parent(i):
    if i!= parent[i]:
        parent[i] = find_parent(parent[i])
    return parent[i]

minimum_spanning_tree_cost = 0
minimum_spanning_tree = []

for edge in edges:
    parent_a = find_parent(edge[1])
    parent_b = find_parent(edge[2])
    if parent_a != parent_b:
        minimum_spanning_tree_cost += edge[3]
        minimum_spanning_tree.append(edge)
        parent[parent_a] = parent_b

print(minimum_spanning_tree_cost)
for edge in minimum_spanning_tree:
    print(edge)




