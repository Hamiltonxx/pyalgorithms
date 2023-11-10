import sys 

for line in sys.stdin:
    res = sum([int(x) for x in line.strip() if not int(x) & 1])
    print(f'{res}\n')