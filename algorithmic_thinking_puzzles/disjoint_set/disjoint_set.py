# class DisjointSet:
#     def __init__(self, n):
#         self.parent = [i for i in range(n)]
#         self.rank = [0] * n 

#     def make_set(self, x):
#         self.parent[x] = x 
#         self.rank[x] = 0

#     def find_set(self, x):
#         if self.parent[x] != x:
#             self.parent[x] = self.find_set(self.parent[x])
#         return self.parent[x]
    
#     def union(self, x, y):
#         x_root = self.find_set(x)
#         y_root = self.find_set(y)
#         if x_root == y_root:
#             return 
#         if self.rank[x_root] > self.rank[y_root]:
#             self.parent[y_root] = x_root 
#         else:
#             self.parent[x_root] = y_root 
#             if self.rank[x_root] == self.rank[y_root]:
#                 self.rank[y_root] += 1


class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def make_set(self, x):
        self.parent[x] = x 

    def find_set(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find_set(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        x_root = self.find_set(x)
        y_root = self.find_set(y)
        if x_root != y_root:
            self.parent[y_root] = x_root

# 创建一个包含10个元素的不相交集
dsu = DisjointSet(10)
# 将元素1和元素2所在的集合合并
dsu.union(1,2)
# 将元素3和元素4所在的集合合并
dsu.union(3,4)
# 将元素1和元素4所在的集合合并
dsu.union(1,4)
# 查找元素2所在的集合的代表元素
print(dsu.find_set(2))
# 查找元素4所在的集合的代表元素
print(dsu.find_set(4))
# 查找元素5所在的集合的代表元素
print(dsu.find_set(5))

