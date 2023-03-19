import bisect
matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target = 5

def f(matrix, target):
    for y in matrix:
        if not y:
            return False
        if y[0] > target:
            return False
        if y[-1] >= target: 
            i = bisect.bisect_left(y, target)
            if y[i] == target:
                return True
    return False

print(f(matrix,target))

