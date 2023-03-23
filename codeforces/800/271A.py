year = input()
y = int(year)
while True:
    y += 1
    st = set(list(str(y)))
    if len(st)==4:
        print(y)
        break

