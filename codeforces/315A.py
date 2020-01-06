n = int(input())

bot,canopen = [],set()
for _ in range(n):
    a,b = map(int,input().split())
    if a==b and a in bot:
        canopen.add(a)
    elif a!=b:
        canopen.add(b)
    bot.append(a)

tmp = 0
for x in bot:
    if x in canopen:
        tmp += 1

print(n-tmp)

