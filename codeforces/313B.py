line = input()
m = int(input())
for _ in range(m):
    l,r = map(int, input().split())
    # s = line[l-1:r]
    cnt = 0
    for i in range(l,r):
        if line[i-1] == line[i]:
            cnt += 1
    print(cnt)