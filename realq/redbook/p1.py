# 题目一：连续子数组最大和
# 小红拿到了一个数组，她希望进行最多一次操作：将一个元素修改为x。小红想知道，最终的连续子数组最大和最大是多少？
# 输入
# 3
# 5 10
# 5 -1 -5 -3 2
# 2 -3
# -5 -2
# 6 10
# 4 -2 -11 -1 4 -1
# 输出
# 15
# -2
# 15
from math import inf
def max_sub_sum(nums, n, x):
    dp0 = [-inf] * n # dp0[i]定义为到i时的未修改的最大和
    dp1 = [-inf] * n # dp1[i]定义为到i时的修改后的最大和
    dp0[0] = nums[0]
    dp1[0] = max(nums[0],x)
    for i in range(1,n):
        dp0[i] = max(dp0[i-1]+nums[i], nums[i])
        dp1[i] = max(dp0[i-1]+x, dp1[i-1]+nums[i])
    return max(max(dp0),max(dp1))

t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    mx = max_sub_sum(arr, n, x)
    print(mx)


