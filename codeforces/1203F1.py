n,r = map(int,input().split())
a = []
for i in range(n):
    a.append(tuple(map(int,input().split())))

a.sort()

# i=0
# b=[]
# while True:
#     if a[i][0]>r:
#         break
#     else:
#         b.append(a[i]) 
#     i += 1 
# b.sort(key=lambda z:-z[1])
while a:
    if a[0][0] > r:
        exit(print("NO"))
    b1,b2 = [],[]
    for x in a:
        if x[0]<=r:
            if x[1]>=0: b1.append(x)
            else: b2.append(x) 
        else:
            break
    mx = max(b,key=lambda z:z[1])
    r += mx[1]
    a.remove(mx)
print("YES")


