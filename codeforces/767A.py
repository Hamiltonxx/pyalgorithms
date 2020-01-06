n = int(input())
lst = list(map(int, input().split()))
s = set()
for i in lst:
    s.add(i)
    while n in s:
        print(n, end=" ")
        n -= 1
    print()