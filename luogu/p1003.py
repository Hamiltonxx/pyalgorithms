n = int(input())
carpet = []
for _ in range(n):
    carpet.append(tuple(map(int, input().split())))
x,y = map(int,input().split())

for i in range(n-1,-1,-1):
    a,b,g,k = carpet[i]
    if a<=x<=a+g and b<=y<=b+k:
        exit(print(i+1))

print(-1)
