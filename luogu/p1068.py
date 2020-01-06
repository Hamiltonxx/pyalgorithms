n,m = map(int,input().split())
m = int(m*1.5)
stu = []
for _ in range(n):
    stu.append(tuple(map(int,input().split())))
stu.sort(key=lambda x:(-x[1],x[0]))

score = stu[m-1][1]
for j in range(m,n):
    if stu[j][1] != score:
        break

print(score, end=" ")
print(j)
for st in stu[:j]:
    print(st[0], end=" ")
    print(st[1])
