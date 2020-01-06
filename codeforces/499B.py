n,m = map(int, input().split())
dic = {}
for i in range(m):
    a,b = input().split()
    if len(b) < len(a):
        dic[a] = b 
lst = input().split()
for x in lst:
    if x in dic:
        print(dic[x],end=" ")
    else:
        print(x,end=" ")