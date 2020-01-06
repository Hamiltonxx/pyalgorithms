def sumdigits(n):
    return sum(list(map(int,list(str(n)))))
    
T = int(input())
for i in range(T):
    N = int(input())
    a0 = list(map(int, input().split()))
    a1 = a0.copy()

    ma = 0
    for x in a0:
        for y in a1:
            if sumdigits(x*y)>ma:
                ma = sumdigits(x*y)
    print(ma)
