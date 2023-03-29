# def maxsubarray(nums):
#     bestsum, currentsum = 0, 0
#     for x in nums:
#         currentsum = max(0, currentsum + x)
#         bestsum = max(bestsum, currentsum)
#     return bestsum

## dp[i] = dp[i-1] + nums[i] if dp[i-1]>0 else nums[i]

def maxsubarray(nums):
    for i in range(1,len(nums)):
        nums[i] = nums[i-1] + nums[i] if nums[i-1]>0 else nums[i]
    return nums

print(maxsubarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))