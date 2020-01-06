T = int(input())
for i in range(T):
    n,m,k = map(int, input().split())
    diff = abs(n-m)
    if diff <= k:
        print(0)
    else:
        print(diff-k)