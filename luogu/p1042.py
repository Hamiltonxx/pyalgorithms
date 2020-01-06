line = input()
while "E" not in line:
    line += input()
s = line.split("E")[0]

a1 = b1 = a2 = b2 = 0
l1,l2 = [],[]

for x in s:
    if x=="W": 
        a1 += 1
        a2 += 1
    if x=="L": 
        b1 += 1
        b2 += 1
    if (a1>=11 or b1>=11) and abs(a1-b1)>1:
        l1.append(f"{a1}:{b1}")
        a1=b1=0
    if (a2>=21 or b2>=21) and abs(a2-b2)>1:
        l2.append(f"{a2}:{b2}")
        a2=b2=0

# if a1 or b1:
l1.append(f"{a1}:{b1}")
# if a2 or b2:
l2.append(f"{a2}:{b2}")

for z in l1:
    print(z)
print()
for z in l2:
    print(z)
