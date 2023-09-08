# # 转化成子集和为 sm//2 的问题
# def canPartition(nums):
#     sm, mx = sum(nums), max(nums)
#     if (sm & 1) or mx*2 > sm: return False
#     if mx*2 == sm: return True
    
#     def exist_subset_sum(nums, target):
#         # dp[i][j]定义为前i个数和为j
#         n = len(nums)
#         dp = [[False]*(target+1) for _ in range(n)]
#         dp[0][nums[0]] = True
#         for i in range(1,n):
#             for j in range(1,target+1):
#                 if nums[i] > j:
#                     dp[i][j] = dp[i-1][j]
#                 else:
#                     dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
#             print(dp[i])
#         return dp[-1][-1]
    
#     return exist_subset_sum(nums, sm//2)

# def canPartition(nums):
#     sm = sum(nums)
#     if sm & 1: return False
#     target = sm // 2
#     dp = [False] * (target+1)
#     dp[0] = True
#     for num in nums:
#         for j in range(target, num-1, -1):
#             dp[j] = dp[j] or dp[j-num]
#     return dp[target]

def canPartition(nums):
    sm = sum(nums)
    if sm & 1: return False
    target = sm // 2
    def exist_subset_sum(nums, target):
        # dp[i]定义为是否存在和为i的子集
        dp = [False] * (target+1)
        dp[0] = True
        for num in nums:
            for i in range(target, num-1, -1):
                dp[i] = dp[i] or dp[i-num]
        return dp[target]
    return exist_subset_sum(nums, target)

print(canPartition([3,3,3,4,5]))