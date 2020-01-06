n = int(input())
trees = []
a = []
b = []
for i in range(n):
    trees.append(tuple(map(int,input().split())))

for i in range(n-1):
    a.append(trees[i+1][0]-trees[i][0])
    if i != n-2:
        b.append(trees[i+1][1])

# m = n-1
# cnt = 0
# for j in range(0,m-1):
#     if a[j] and a[j] > b[j]:
#         cnt += 1
#         a[j] = 0
#     elif a[j+1] and a[j+1] > b[j]:
#         cnt += 1
#         a[j+1] = 0

# print(cnt+2)
cnt = 0
m = n-2
for i in range(m):
    if  b[i] < a[i]:
        cnt += 1
        a[i] = 0
    elif b[i] < a[i+1]:
        cnt += 1
        a[i+1] = 0

print(cnt+2)


