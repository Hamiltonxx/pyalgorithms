import sys 

for line in sys.stdin:
    m,k = map(int, line.split())
    if m==k==0: exit()
    q,r = divmod(m,k)
    res = m + q
    while q+r >= k:
        q,r = divmod(q+r,k)
        res += q
    print(res)

