M,N,K = map(int,input().split())
L = []
for i in range(M):
    lst = list(map(int,input().split()))
    for j,p in enumerate(lst):
        if p > 0:
            L.append((p,i,j))

L.sort(reverse=True)

s=0
x,y = 0,0
if (L[0][1]+1)*2+1 <= K:
    s += L[0][0]
    K -= L[0][1]+2
    x,y = L[0][1],L[0][2]
else:
    exit(print(0))
    
for p,i,j in L[1:]:
    if abs(x-i)+abs(y-j)+i+1+1 <= K:
        s += p 
        K -= abs(x-i)+abs(y-j)+1
        x,y = i,j
    else:
        break

print(s)
