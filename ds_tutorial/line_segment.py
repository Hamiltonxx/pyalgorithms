n = input()
a = []
for _ in range(n):
    x,y = map(int,input().split())
    if x>y:
        x,y = y,x
    a.append((x,y))
a.sort(key=lambda z:z[1])

cnt = 1
tmp = a[0][1]
for x in a[1:]:
    if tmp <= x[0]:
        cnt += 1
        tmp = x[1]

print(cnt)