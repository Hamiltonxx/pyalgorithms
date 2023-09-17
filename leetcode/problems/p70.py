# 最多能用 n//2 次两阶步
# n=3时，0两阶: 1,1,1; 1两阶: 2,1 1,2
# n=4时，0两阶: 1,1,1,1; 1两阶: 2,1,1 1,2,1 1,1,2; 2两阶: 2,2
# 随着2阶步数的增加，我们计算2阶步的不同位置数即可
# import math
# def climbStairs(n):
#     cnt = 0
#     for st2 in range(n//2+1):
#         cnt += math.comb(n-st2, st2)
#         # 可以理解为往n-step2个坑里放step2个2
#     return cnt 

# 完全背包
def climb_stairs(n):
    dp = [0] * (n+1)
    dp[0] = 1
    for j in range(1, n+1):
        for step in [1,2]:
            if j >= step:
                dp[j] += dp[j-step]
    return dp[n]

print(climb_stairs(2))
print(climb_stairs(3))
print(climb_stairs(4))