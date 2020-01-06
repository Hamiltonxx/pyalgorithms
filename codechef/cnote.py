T = int(input())
for i in range(T):
    X,Y,K,N = map(int, input().split())
    left = X-Y
    flag=0
    for j in range(N):
        P,C = map(int, input().split())
        if left<=P and C<=K and flag==0:
            flag=1
    print("LuckyChef") if flag else print("UnluckyChef")

