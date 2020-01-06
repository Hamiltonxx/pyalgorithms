def findIndex(lst,item):
    try:
        idx = lst.index(item)
        return idx
    except:
        return -1

N = int(input())
a = [1]
for i in range(2,N+1):
    num,lr = map(int,input().split())
    idx = findIndex(a,num)

    a = a[:idx+lr] + [i] + a[idx+lr:]

M = int(input())
for _ in range(M):
    x = int(input())
    idx = findIndex(a,x)
    if idx > -1:
        a = a[:idx] + a[idx+1:]

print(*a)

