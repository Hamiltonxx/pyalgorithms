T = int(input())
cnt = 0
for i in range(T):
    line = input()
    if "ch" in line or "he" in line or "ef" in line:
        cnt += 1
print(cnt)