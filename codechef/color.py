T = int(input())
for i in range(T):
    n = int(input())
    line = input()
    cntR = line.count('R')
    cntG = line.count('G')
    cntB = n - cntR - cntG 
    a = max(cntR, cntG, cntB)
    print(n-a)
