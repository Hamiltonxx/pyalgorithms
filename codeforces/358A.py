n = int(input())
lst = list(map(int,input().split()))

a = list(zip(lst,lst[1:]))

record = []

for x in a:
    s,e = min(x[0],x[1]),max(x[0],x[1])
    for y in record:
        if y[0]<s<y[1]<e or s<y[0]<e<y[1]:
            exit(print("yes"))
    record.append((s,e))
print("no")


