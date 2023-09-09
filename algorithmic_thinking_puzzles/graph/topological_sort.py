graph = { # DAG
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}

from collections import deque 

def topological_sort(graph):
    # 第一步: 计算所有顶点的入度
    in_degrees = {vertex: 0 for vertex in graph}
    for vertex in graph:
        for neighbor in graph[vertex]:
            in_degrees[neighbor] += 1

    # 第二步：执行拓扑排序
    queue = deque()
    for vertex in graph:
        if in_degrees[vertex] == 0:
            queue.append(vertex)

    topological_order = []
    while queue:
        vertex = queue.popleft()
        topological_order.append(vertex)

        for neighbor in graph[vertex]:
            in_degrees[neighbor] -= 1
            if in_degrees[neighbor] == 0:
                queue.append(neighbor)

    return topological_order

# result = topological_sort(graph)
# print(result)

def topsort(graph): # --> List
    indeg = {v:0 for v in graph}
    for v in graph:
        for u in graph[v]:
            indeg[u] += 1

    q = deque()
    for v in graph:
        if indeg[v] == 0:
            q.append(v)

    order = []
    while q:
        v = q.popleft()
        order.append(v)
        for u in graph[v]:
            indeg[u] -= 1
            if indeg[u] == 0:
                q.append(u)

    return order
