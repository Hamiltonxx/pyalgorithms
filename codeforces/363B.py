n,k = map(int,input().split())
p = list(map(int, input().split()))

pos = 0
mi = s = sum(p[:k])

for i in range(k,n):
    s += p[i]
    s -= p[i-k]
    if s < mi:
        mi = s 
        pos = i-k+1

print(pos+1)