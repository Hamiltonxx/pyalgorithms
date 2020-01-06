n = int(input())
a = list(map(int,input().split()))

a.sort()
s = sum(a)
t = s*2
for x in a:
    s = s-x
    t += s
t -= x 

print(t)
