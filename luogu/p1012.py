n = int(input())
a = input().split()

b = []
mx = 0
for x in a:
    if len(x)>mx: mx=len(x)
for x in a:
    y = x+x[-1]*(mx-len(x))
    b.append((y,x))

b.sort(reverse=True)
c = [x[1] for x in b]

print("".join(c))