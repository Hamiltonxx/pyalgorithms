from math import inf
# def max_sub_sum(nums):
#     # dp[i]定义为到i时的最大和(并不需要从0开始算)
#     n = len(nums)
#     dp = nums
#     for i in range(1,n):
#         dp[i] = max(dp[i-1]+nums[i], nums[i])
#     return max(dp)

def max_sub_sum(nums):
    n = len(nums)
    for i in range(1,n):
        nums[i] = max(nums[i-1]+nums[i], nums[i])
    return max(nums)

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_sub_sum(nums))
