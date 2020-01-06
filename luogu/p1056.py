from collections import Counter

M,N,K,L,D = map(int, input().split())

row = []
col = []

for _ in range(D):
    x,y,p,q = map(int, input().split())
    if x==p: col.append(min(y,q))
    if y==q: row.append(min(x,p))

c0 = Counter(row).most_common()
c1 = Counter(col).most_common()

k = [x[0] for x in c0]
l = [x[0] for x in c1]

print(" ".join(map(str,sorted(k[:K]))))
print(" ".join(map(str,sorted(l[:L]))))
