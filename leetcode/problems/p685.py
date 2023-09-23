# def findRedundantDirectedConnection(edges):
#     n = len(edges)
#     parent = list(range(n+1))

#     def find(x):
#         if parent[x] != x:
#             parent[x] = find(parent[x])
#         return parent[x]
#     # def union(x,y):
#     #     xroot,yroot = find(x),find(y)
#     #     if xroot != yroot:
#     #         parent[yroot] = xroot
#         #     return False
#         # return True

#     last, can = None, []
#     p = {}
#     for u,v in edges:
#         if v in p:
#             can.append([p[v],v])
#             can.append([u,v])
#         else:
#             p[v] = u
#             # if union(u,v):
#             #     last = [u,v]
#             uroot, vroot = find(u), find(v)
#             if uroot == vroot:
#                 last = [u,v]
#             else: # union
#                 parent[vroot] = uroot
#     if not can:
#         return last
#     return can[0] if last else can[1]

# 得考虑三种情况. 
# [1,2],[2,3],[3,1],[4,2] 双父有环,返回前边 (点2双父，前边[1,2])
# [1,2],[1,3],[2,3] 双父无环,返回后边 (点3双父，后边[2,3])
# [1,2],[2,3],[3,1] 无双父(必有环), 返回最后一边

def findRedundantDirectedConnection(edges):
    n = len(edges)
    parent = list(range(n+1))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    last, can = None, []
    p = {}
    for u,v in edges:
        if v in p: # 双父
            can.append([p[v],v])  # 前
            can.append([u,v])  # 后
        else:
            p[v] = u
            uroot, vroot = find(u), find(v)
            if uroot == vroot: # 有环
                last = [u,v]
            else: # union
                parent[vroot] = uroot
    if not can: # 无双父
        return last
    return can[0] if last else can[1]