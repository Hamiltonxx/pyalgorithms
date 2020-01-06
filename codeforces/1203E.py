n = int(input())
a = list(map(int,input().split()))

a.sort()

team = [a[0]-1] if a[0]>1 else [a[0]]
for x in a[1:]:
    if x-1>team[-1]:
        team.append(x-1)
    elif x>team[-1]:
        team.append(x)
    elif x+1>team[-1]:
        team.append(x+1)

print(len(team))