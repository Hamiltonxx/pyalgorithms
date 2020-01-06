N = int(input())
stu = []
total = 0
for i in range(N):
    name,score,cla,leader,west,paper = input().split()
    score = int(score)
    cla = int(cla)
    leader = 1 if leader=="Y" else 0
    west = 1 if west=="Y" else 0
    paper = int(paper)
    sh = 0
    if score>80 and paper: sh += 8000
    if score>85 and cla>80: sh += 4000
    if score>90: sh += 2000
    if score>85 and west: sh += 1000
    if cla>80 and leader: sh += 850
    stu.append((sh,i,name))
    total+=sh

res = max(stu, key=lambda st:(st[0],-st[1]))
print(res[2])
print(res[0])
print(total)