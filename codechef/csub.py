t = int(input())
for i in range(t):
    input()
    line = input()
    n = line.count('1')
    res = sum(range(1,n+1))
    print(res)