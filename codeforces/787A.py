a,b = map(int, input().split())
c,d = map(int, input().split())

for i in range(b,10**4,a):
    if i in range(d,10**4,c):
        exit(print(i))
print(-1)
