n = int(input())
line = input()

s=""
for x in line:
    t = ord(x)+n
    if t>ord('z'): t = ord('a') + t - ord('z') -1
    s += chr(t)
print(s)