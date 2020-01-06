s = input()
t = input()
p = input()

a,b = [],[]

for i in range(len(s)):
    if s[i] not in a and t[i] not in b:
        a.append(s[i])
        b.append(t[i])
    elif (s[i] in a and t[i] not in b) or (s[i] not in a and t[i] in b) or (a.index(s[i])!=b.index(t[i])):
        exit(print("Failed"))

res=""
if len(b)<26:
    res="Failed"
else:
    for x in p:
        res += t[s.index(x)]

print(res)