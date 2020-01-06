n = int(input())
a = list(map(int, input().split()))

maxlen = curlen = 1
for i in range(1,n):
    if a[i]>=a[i-1]:
        curlen += 1
    else:
        if maxlen < curlen:
            maxlen = curlen 
        curlen = 1
if maxlen < curlen: 
    maxlen = curlen
print(maxlen)
