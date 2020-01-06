from collections import defaultdict

a = input()
b = input()

a = list(pattern)
b = str.split(" ")
if len(a)!=len(b):
    return False
l = len(a)
d1, d2 = defaultdict(list),defaultdict(list)
for i in range(l):
    if (a[i] not d1 and b[i] not in d2) or (a[i] in d1 and b[i] in d2 and d1[a[i]] == d2[b[i]]):
        d1[a[i]].append(i)
        d2[b[i]].append(i)
    else:
        return False
return True