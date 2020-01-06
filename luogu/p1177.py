N=int(input())
a = list(map(int,input().split()))
a.sort()
for x in a[:N-1]:
    print(x,end=" ")
print(a[-1])