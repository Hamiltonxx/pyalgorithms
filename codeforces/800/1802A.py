t = int(input())
for _ in range(t):
    n = int(input())
    neg = input().count("-")
    pos = n - neg
    maxrange = list(range(1,pos+1)) + list(range(pos-1,pos-neg-1,-1))
    minrange = [1,0]*neg + list(range(1,pos-neg+1))
    print(*maxrange)
    print(*minrange)
