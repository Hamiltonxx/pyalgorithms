a = [0,1]
n = 38
for i in range(2,n):
    a[i] = (a[i-1]+a[i-2]) % 1000000007
    