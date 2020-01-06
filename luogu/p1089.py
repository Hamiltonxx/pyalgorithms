remain = deposit = 0
for i in range(12):
    a = int(input())
    remain = remain+300-a
    if remain < 0:
        exit(print(-i-1))
    deposit += remain//100
    remain = remain%100

print(deposit*120+remain)