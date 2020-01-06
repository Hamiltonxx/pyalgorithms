remain = deposit = 0
bankrupt = False

for i in range(12):
    a = int(input())
    remain = remain+300-a
    if remain < 0:
        bankrupt = True 
        break 
    deposit += remain//100
    remain = remain%100

if bankrupt:
    print(-i-1)
else:
    print(deposit*120+remain)