n,k = map(int,input().split())
a = list(map(int, input().split()))

d = 0
for i in range(1,len(a)-2):
    if a[i-1]+a[i]<k:
        d += k-a[i-1]-a[i]
 
        if a[i-1]<a[i+1] and a[i]>=a[i+2]:
            a[i-1] = k - a[i]
        else:
            a[i] = k - a[i-1]
if a[-3]+a[-2] < k:
    d += k-a[-3]-a[-2]
    if a[-3] < a[-1]:
        a[-3] = k - a[-2]
    else:
        a[-2] = k - a[-3]
if a[-1]+a[-2] < k:
    d += k-a[-1]-a[-2]
    a[-1] = k - a[-2]

print(d)
for x in a:
    print(x, end=" ")


