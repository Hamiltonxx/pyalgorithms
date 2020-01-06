n = int(input())
a = list(map(int,input().split()))
t = []
for i,x in enumerate(a):
    t.append((x,i+1))
t.sort()
p,q = zip(*t)
print(*q)

T=0
for i in range(n):
    T += p[i] * (n-i-1)
print("{:.2f}".format(T/n))