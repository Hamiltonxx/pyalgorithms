N,T = map(int,input().split())
a = []
for _ in range(N):
    a.append(int(input()))

a.sort(reverse=True)

i,j = 0,N-1
k=0
while j>i:
    s = a[i]
    while s+a[j]<=T and j>=i:
        j -= 1
        s += a[j]
    k += 1
    i += 1

print(k)