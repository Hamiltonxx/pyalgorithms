n,k = map(int, input().split())
p = 0
for p in range(1,20):
    k += p*5 
    if k > 240:
        break
print(min(n,p-1))