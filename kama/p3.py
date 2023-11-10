import sys

for line in sys.stdin:
    a,b = map(int, line.split())
    if a == b == 0:
        exit()
    print(a + b)