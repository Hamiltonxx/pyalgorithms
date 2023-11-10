import sys

for line in sys.stdin:
    arr = list(map(int, line.split()))
    if arr[0] == 0:
        exit()
    print(sum(arr[1:]))