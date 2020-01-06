w = int(input())
n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

cnt=0
a.sort(reverse=True)
i,j = 0,n-1
while j>i:
    if a[i]+a[j]<=w:
        i += 1
        j -= 1
    else:
        i += 1
    cnt += 1
if i==j:
    cnt += 1
print(cnt)