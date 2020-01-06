n,m = map(int,input().split())
guy = []
for _ in range(n):
    a,b = input().split()
    guy.append((int(a),b))

p = 0
for _ in range(m):
    x,y = map(int, input().split())
    flag = [-1,1][guy[p][0]^x]
    p += flag*y
    if p>n-1: p -= n
    if p<0: p += n

print(guy[p][1])
