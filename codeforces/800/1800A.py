import re 
t = int(input())
for _ in range(t):
    input()
    print("YES" if re.match("^[Mm]+[Ee]+[Oo]+[Ww]+$", input()) else "NO")
    