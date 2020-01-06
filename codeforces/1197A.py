t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    if n<3 or a[1] < 2:
        print(0)
    else:
        if a[1]-1 <= n-2:
            print(a[1]-1)
        else:
            print(n-2)

