n = int(input())
a = []
for _ in range(n):
    a.append(tuple(map(int,input().split())))
a.sort(key=lambda z:z[1])

cnt=tmp=0
for x in a:
    if tmp<=x[0]:
        cnt += 1
        tmp = x[1]

print(cnt)