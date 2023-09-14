# 完全背包
import math
# def numSquare(n):
#     dp = [float('inf')] * (n+1)
#     dp[0] = 0
#     m = math.isqrt(n)
#     for num in range(1,m+1):
#         for j in range(num**2,n+1):
#             dp[j] = min(dp[j], dp[j-num**2]+1)
#     return dp[n]

# print(numSquare(12))
# print(numSquare(13))

# Langrage's 4 Square theorem
def numSquare(n):
    def is_perfect_square(n):
        return math.isqrt(n) ** 2 == n
    cpy_n = n 
    if is_perfect_square(n):
        return 1
    while n & 3 == 0: # divisible by 4
        n >>= 2 # divided by 4
    if n & 7 == 7: # n % 8 == 7
        return 4
    n = cpy_n 
    for i in range(1, math.isqrt(n)+1):
        if is_perfect_square(n - i**2):
            return 2
    return 3