line = input()
l=len(line)
k = int(input())
s = list(map(int,input().split()))

ma = max(s)
ans = 0
for i,x in enumerate(line):
    ans += s[ord(x)-ord('a')]*(i+1)
for j in range(k):
    ans += ma * (l+j+1)
print(ans)
