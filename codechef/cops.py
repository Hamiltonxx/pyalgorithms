t = int(input())
for i in range(t):
    m,x,y = map(int, input().split())
    resides = map(int, input().split())
    z = x*y
    covers = set()
    for r in resides:
        covers = covers | set(range(r-z, r+z+1))
    total = set(range(1,101))
    print(len(total-covers))