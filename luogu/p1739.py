line = input()

cntl = 0
for x in line:
    if x=="(":
        cntl += 1
    elif x==")":
        if cntl == 0:
            exit(print("NO"))
        cntl -= 1
    elif x=="@":
        break
if cntl==0:
    print("YES")
else:
    print("NO")