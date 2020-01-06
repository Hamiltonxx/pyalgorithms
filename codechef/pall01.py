t = int(input())

for i in range(t):
    line = input()
    if int(line) == int(line[::-1]):
        print("wins")
    else:
        print("losses")
