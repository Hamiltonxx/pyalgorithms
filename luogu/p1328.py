from collections import deque 

N,Na,Nb = map(int,input().split())
if Na==1: Ca = deque([int(input())])
else: Ca = deque(map(int, input().split()))
if Nb==1: Cb = deque([int(input())])
else: Cb = deque(map(int,input().split()))
res = [[0,0,1,1,0],
       [1,0,0,1,0],
       [0,1,0,0,1],
       [0,0,1,0,1],
       [1,1,0,0,0]]

sa = sb = 0

for _ in range(N):
    a = Ca.popleft()
    b = Cb.popleft()
    sa += res[a][b]
    sb += res[b][a]
    Ca.append(a)
    Cb.append(b)

print(f"{sa} {sb}")
