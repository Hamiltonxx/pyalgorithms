from collections import deque 

M,N = map(int, input().split())
w = map(int, input().split())

Q = deque([])
ans = 0
for x in w:
    if x not in Q:
        ans += 1
        if len(Q)==M:
            Q.popleft()
        Q.append(x)

print(ans)
