n,m = map(int,input().split())
lst = list(map(int,input().split()))

lst.sort()

mi = lst[n-1] - lst[0]
for i in range(m-n+1):
    if lst[i+n-1]-lst[i] < mi:
        mi = lst[i+n-1] - lst[i]
print(mi)