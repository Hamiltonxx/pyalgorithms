line = input()
l = len(line)
a = [0] * l
for i in range(1,l):
    a[i] = a[i-1] + (line[i]==line[i-1])
m = int(input())
ans = ''
for _ in range(m):
    l,r = map(int,input().split())
    ans += str(a[r-1]-a[l-1])+'\n'
print(ans)
