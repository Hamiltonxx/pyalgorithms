T = int(input())
for i in range(T):
    input()
    a = list(map(int,input().split()))
    min0 = min(a)
    a.remove(min0)
    min1 = min(a)
    print(min0+min1)