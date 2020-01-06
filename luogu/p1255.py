#f[n] = f[n-1] + f[n-2]

N = int(input())
if N==0:
    exit(print(0))
a = [1,1]
for i in range(2,N+1):
    a.append(a[i-1]+a[i-2])

print(a[N])
