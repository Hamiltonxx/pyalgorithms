# def partitionLabels(s):
#     d = {c:i for i,c in enumerate(s)}
#     print(d)
#     mx, size, res = 0, 0, []
#     for i,c in enumerate(s):
#         size += 1
#         mx = max(mx, d[c])

#         if i == mx:
#             res.append(size)
#             size = 0
    
#     return res

# def partitionLabels(s):
#     d = {c:idx for idx,c in enumerate(s)}
#     i, j = 0, 0
#     ans = []

#     for idx,c in enumerate(s):
#         j = max(j, d[c])
#         if i == j:
#             ans.append(j-i+1)
#             i = idx + 1

#     return ans

def partitionLabels(s):
    cnt, res = 0, []
    for i in range(1, len(s)+1):
        cnt += 1
        if not (set(s[:i]) & set(s[i:])):
            res.append(cnt)
            cnt = 0
    return res

s = "ababcbacadefegdehijhklij"
print(partitionLabels(s))