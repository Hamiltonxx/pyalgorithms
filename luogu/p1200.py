a = input()
b = input()
n = m = 1
for x in a:
    n *= ord(x)-ord('A')+1
for y in b:
    m *= ord(y)-ord('A')+1

if n % 47 == m % 47:
    print("GO")
else:
    print("STAY")