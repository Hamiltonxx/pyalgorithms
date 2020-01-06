q = int(input())
for _ in range(q):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    ans="YES"
    b = a[:2*n]
    c = a[2*n:]
    c = c[::-1]
    area = a[0]*a[-1]
    for i in range(n):
        if b[i*2]!=b[i*2+1] or c[i*2]!=c[i*2+1] or b[i*2]*c[i*2]!=area:
            ans = "NO"
            break
    print(ans)
