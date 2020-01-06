t = int(input())
for i in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    base = min(lst)
    total = 0
    for x in lst:
        total += x-base
    print(total)
