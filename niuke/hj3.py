n = int(input())
s = set()
for _ in range(n):
    s.add(int(input()))
l = list(s)
l.sort()
for x in l:
    print(x)
