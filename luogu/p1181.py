N,M = map(int,input().split())
a = list(map(int,input().split()))

s = cnt = 0
for x in a:
    s += x
    if s > M:
        s = x
        cnt += 1
        
print(cnt+1)