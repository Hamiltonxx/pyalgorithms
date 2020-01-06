T = int(input())
for i in range(T):
    n,k = map(int, input().split())
    ma = 0
    for i in range(1,k+1):
        if n%i > ma:
            ma = n%i 
    print(ma)