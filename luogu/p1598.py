from collections import Counter
line = input()+input()+input()+input()
s = ""
for x in line:
    if 'A'<=x<='Z':
        s += x 
c = Counter(s)
mx = c.most_common()[0][1]

lst = []
for ch in range(ord('A'),ord('Z')+1):
    k = c[chr(ch)]
    lst.append(" "*(mx-k)+"*"*k)
trans = list(zip(*lst))

for x in trans:
    print(" ".join(x))
print(*("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))