T = int(input())
for i in range(T):
    N = int(input())
    full = []
    first = []
    for j in range(N):
        stu = input().split()
        full.append(stu)
        first.append(stu[0])
    for x in full:
        if first.count(x[0]) > 1:
            print(x[0]+" "+x[1])
        else:
            print(x[0])





