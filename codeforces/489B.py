n = int(input())
b = list(map(int, input().split()))
m = int(input())
g = list(map(int, input().split()))

b.sort()
g.sort()

cnt = 0
while b and g:
    if b[-1] - g[-1] > 1:
        b.pop()
    elif g[-1] - b[-1] > 1:
        g.pop()
    else:
        cnt += 1
        b.pop()
        g.pop()
print(cnt)