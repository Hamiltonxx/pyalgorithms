# 1 2 3
# 4 5 6
# 7 8 9

#  1  2  3  4
#  5  6  7  8
#  9 10 11 12
# 13 14 15 16

matrix =  [[1,  2,  3,  4,  5],
           [6,  7,  8,  9, 10],
           [11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20]]

def clockwise(matrix):
    res = []
    while matrix:
        t = matrix.pop(0)
        res += t
        matrix = list(zip(*matrix))[::-1]
    return res

print(clockwise(matrix))