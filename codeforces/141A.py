names = input() + input()
letters = input()

dic1 = {}
dic2 = {}

for x in names:
    if x in dic1:
        dic1[x] += 1
    else:
        dic1[x] = 1
for y in letters:
    if y in dic2:
        dic2[y] += 1
    else:
        dic2[y] = 1
        
if dic1 == dic2:
    print("YES")
else:
    print("NO")