from itertools import combinations

s = input()

for x in s:
    if int(x)%8==0:
        exit(print("YES\n"+x))
for i,j in combinations(range(len(s)),2):
    if int(s[i]+s[j])%8==0:
        exit(print("YES\n"+s[i]+s[j]))
for i,j,k in combinations(range(len(s)),3):
    if int(s[i]+s[j]+s[k])%8==0:
        exit(print("YES\n"+s[i]+s[j]+s[k]))
print("NO")
