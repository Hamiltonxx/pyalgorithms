n,m = map(int,input().split())
a = list(map(int,input().split()))
s = set()
for i in range(n-1,-1,-1):
    s.add(a[i])
    a[i] = len(s)
for _ in range(m):
    l = int(input())-1
    print(a[l])