n = int(input())
stu = []
for i in range(n):
    ch,mt,en = map(int,input().split())
    stu.append((ch+mt+en,ch,i))

stu.sort(key=lambda st:(-st[0],-st[1],st[2]))

for j in range(5):
    print(f"{stu[j][2]+1} {stu[j][0]}")