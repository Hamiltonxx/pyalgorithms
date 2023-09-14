# def rob(nums):
#     n = len(nums)
#     dp = [0] * n
#     dp[0], dp[1] = nums[0], max(nums[:2])
#     for i in range(2,n):
#         dp[i] = max(dp[i-1], dp[i-2]+nums[i])
#     return dp[-1]

# def rob(nums):
#     pre, cur = 0, nums[0]
#     for x in nums[1:]:
#         pre, cur = cur, max(pre+x, cur)
#     return cur

def rob(nums):
    pre = cur = 0
    for num in nums:
        pre, cur = cur, max(pre+num, cur)
    return cur