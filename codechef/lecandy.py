T = int(input())
for i in range(T):
    C = list(map(int, input().split(" ")))[1]
    total = sum(list(map(int,input().split(" "))))
    if total > C:
        print("No")
    else:
        print("Yes")
        