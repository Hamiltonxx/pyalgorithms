if __name__ == '__main__':
    # Accept No. of Nodes and edges
    n,m = map(int,input().split())

    # Dictionary of edges
    g = {}
    for i in range(n):
        g[i+1] = []

    # Accepting edges of Unweighted Directed Graphs
    for _ in range(m):
        x, y = map(int, input().split())
        g[x].append(y)

    # Accepting edges of Unweighted Undirected Graphs
    for _ in range(m):
        x, y = map(int, input().split())
        g[x].append(y)
        g[y].append(x)

    # Accepting edges of Weighted Undirected Graphs
    for _ in range(m):
        x,y,r = map(int, input().split())
        g[x].append([y,r])
        g[y].append([x,r])

    """ Depth First Search
            Args: G - Dictionary of edges
                  s - Starting Node
            Vars: vis - Set of visited nodes
                  S - Traversal Stack """
    def dfs(G,s):
        vis, S = set([s]), [s]
        print(s)
        while S:
            flag = 0
            for v in G[S[-1]]:
                if v not in vis:
                    S.append(v)
                    vis.add(v)
                    flag = 1
                    print(v)
                    break 
            if not flag:
                S.pop()

    """ Breadth First Search
            Args: G - Dictionary of edges
                  s - Starting Node
            Vars: vis - Set of visited nodes
                  S - Traversal Stack """
    from collections import deque
    def bfs(G,s):
        vis, Q = set([s]), deque([s])
        print(s)
        while Q:
            u = Q.popleft()
            for v in G[u]:
                if v not in vis:
                    vis.add(v)
                    Q.append(v)
                    print(v)

    """ Dijkstra's shortest path algorithm
            