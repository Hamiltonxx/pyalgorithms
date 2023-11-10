import sys 

for line in sys.stdin:
    arr = list(map(int, line.split()))
    if len(arr) == 2:
        print(sum(arr))