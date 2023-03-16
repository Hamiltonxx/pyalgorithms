import sys  

rl = list(range(1235))
cl = list(range(5679))

for line in sys.stdin:
    cmd = line.split()
    if cmd[0]=="W":
        num = int(cmd[1])
        x,y = num//5678+1, num%5678
        print(rl.index(x), cl.index(y))
    else:
        x,y = int(cmd[1]), int(cmd[2])
        if cmd[0]=="R":
            rl[x], rl[y] = rl[y], rl[x]
        elif cmd[0]=="C":
            cl[x], cl[y] = cl[y], cl[x]
        elif cmd[0]=="Q":
            x,y = rl[x],cl[y]
            print(5678*(x-1)+y) 