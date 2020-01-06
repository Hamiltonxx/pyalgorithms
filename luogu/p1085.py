mx = 0
day = 0
for i in range(7):
    a,b = map(int,input().split())
    if a+b > mx:
        mx = a+b
        day = i+1
if mx >= 8:
    print(day)
else:
    print(0)