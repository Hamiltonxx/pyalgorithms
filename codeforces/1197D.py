n,m,k = map(int, input().split())
a = list(map(int,input().split()))
ma = 0
for j in range(n-1,n-m-1,-1):
    c = 0
    s = 0
    for i in range(j,-1,-1):
        s += a[i]
        ma = max(ma,s-c-k)
        if (j-i+1)%m==0:
            s -= k
        if s<c:
            c = s 

print(ma)