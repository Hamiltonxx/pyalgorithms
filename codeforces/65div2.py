n = int(input())
for i in range(n):
    line = input()
    if len(line) <= 10:
        print(line)
    else:
        print(line[0]+str(len(line)-2)+line[-1])