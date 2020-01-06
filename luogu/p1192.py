# f(n) = f(n-1) + f(n-2) + ... + f(n-k)

N,K = map(int,input().split())
md = 100003

a = [1]*(N+1) 

for i in range(1,N+1):
    if i<=K:
        a[i] = 2**(i-1) % md
    else:
        a[i] = (2*a[i-1] - a[i-K-1]) % md

print(a[N])
