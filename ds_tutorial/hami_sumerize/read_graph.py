# 读图
from collections import defaultdict

# 节点数和边数
n,m = map(int, input().split())
# 边字典图
g = defaultdict(list)

# 无权有向图
# for _ in range(m):
#     x,y = map(int, input().split())
#     g[x].append(y)

# 无权无向图
for _ in range(m):
    x,y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)

# 有权无向图
# for _ in range(m):
#     x,y,d = map(int, input().split())
#     g[x].append((y,d))
#     g[y].append((x,d))

# print(g)
# print(g[2])