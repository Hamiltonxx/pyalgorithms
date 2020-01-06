t = int(input())
for i in range(t):
    ch = input()
    if ch == 'B' or ch == 'b':
        print("BattleShip")
    elif ch == 'C' or ch == 'c':
        print("Cruiser")
    elif ch == 'D' or ch == 'd':
        print('Destroyer')
    else:
        print("Frigate")