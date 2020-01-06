N,M = map(int,input().split())
mk = []
for _ in range(M):
    p,q = map(int,input().split())
    mk.append((p,q))
mk.sort(key=lambda z:(z[0],-z[1]))
P=Q=0
for x in mk:
    if Q+x[1]>N:
        P += (N-Q)*x[0]
        break
    else:
        Q += x[1]
        P += x[0]*x[1]
print(P)
