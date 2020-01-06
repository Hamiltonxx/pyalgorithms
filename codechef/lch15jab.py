T = int(input())
for i in range(T):
    line = input()
    if len(line) % 2:
        print("NO")
    else:
        lst = [0]*26
        for ch in line:
            lst[ord(ch)-ord('a')] += 1
        if len(line)//2 in lst:
            print("YES")
        else:
            print("NO")
