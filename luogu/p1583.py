n,k = map(int,input().split())
E = list(map(int, input().split()))
W = list(map(int, input().split()))

w = []
for i,x in enumerate(W):
    w.append((x,i))

w.sort(key=lambda z:(-z[0],z[1]))

d = []
for j,y in enumerate(w):
    d.append((y[0]+E[j%10],y[1]))

d.sort(key=lambda z:(-z[0],z[1]))

res = [x[1]+1 for x in d[:k]]
print(*res)