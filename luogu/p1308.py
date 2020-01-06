a = input().upper()
s = input().upper()
b = s.split()

if a in b:
    k = b.count(a)
    print(k, end=" ")
    if s.startswith(a):
        print(0)
    elif s.endswith(a) and k==1:
        print(s.index(" "+a)+1)
    else:
        print(s.index(" "+a+" ")+1)

else:
    print(-1)