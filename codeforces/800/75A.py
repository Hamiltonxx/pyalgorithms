a = input()
aa = a.replace("0","")
b = input()
bb = b.replace("0","")
c = int(a)+int(b)
cc = str(c).replace("0","")
if int(cc) == int(aa) + int(bb):
    print("YES")
else:
    print("NO")
