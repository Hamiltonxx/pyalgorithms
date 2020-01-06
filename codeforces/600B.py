import bisect 
n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
b = list(map(int,input().split()))
for x in b:
    print(bisect.bisect(a,x),end=" ")