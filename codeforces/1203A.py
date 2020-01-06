q = int(input())
for _ in range(q):
    n = int(input())
    stu = list(map(int,input().split()))
    k = stu[0]
    if stu==list(range(k,n+1)) + list(range(1,k)) or stu==list(range(k,0,-1))+list(range(n,k,-1)):
        print("YES")
    else:
        print("NO")

