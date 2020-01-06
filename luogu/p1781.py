n = int(input())
a = []
for i in range(n):
    a.append((input(),i))

p = max(a, key=lambda x:(len(x[0]),x[0]))

print(p[1]+1)
print(p[0])