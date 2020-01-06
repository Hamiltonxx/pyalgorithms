t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    languages = input().split()
    phases = []
    for j in range(k):
        phases += input().split()[1:]
    for x in languages:
        if x in phases:
            print("YES", end=" ")
        else:
            print("NO", end=" ")
