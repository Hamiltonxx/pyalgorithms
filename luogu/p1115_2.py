input()
a = list(map(int,input().split()))

res = s = a[0]
for x in a[1:]:
    if s<0: s=0
    s += x
    res = max(res,s)
print(res)