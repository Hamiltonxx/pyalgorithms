import sys 

for line in sys.stdin:
    arr = list(map(int, line.split()))
    if len(arr) == 1:
        N = arr[0]
    else:
        print(sum(arr[1:]))
        if N > 1:
            print()
        N -= 1