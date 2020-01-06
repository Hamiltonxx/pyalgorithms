n = int(input())
line = input()

if "HH" in line:
    print("NO")
else:
    print("YES")
    print(line.replace(".","B"))
