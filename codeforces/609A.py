n = int(input())
m = int(input())
fd = [int(input()) for _ in range(n)]
fd.sort(reverse=True)
cnt = 0
for x in fd:
    cnt += 1
    m -= x
    if m <= 0:
        break
print(cnt)

