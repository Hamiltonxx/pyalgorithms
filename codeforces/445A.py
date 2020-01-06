n,m = map(int, input().split())
for i in range(n):
    row = list(input())
    for j in range(m):
        if row[j]=='.':
            row[j]='W' if (i+j)%2 else 'B'
    print("".join(row))
        
