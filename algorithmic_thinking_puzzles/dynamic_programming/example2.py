from functools import lru_cache
# 切批萨方案*
# 这问题需要再复习， P1444
# 还有分批萨， P1388

# Maximum sum such that no two elements are adjacent.
# [5,5,10,100,10,5] -> 110  [3,2,7,10] -> 13  [3,2,5,10,7] -> 15
# def findMaxSum(arr):
#     n = len(arr)
#     @lru_cache(None)
#     def rec(nums,idx=0):
#         if idx >= n:
#             return 0
#         return max(nums[idx]+rec(nums,idx+2), rec(nums, idx+1))
#     return rec(tuple(arr))

def findMaxSum(arr):
    n = len(arr)
    if len(arr)<3:
        return max(arr)
    dp = [arr[0],max(arr[:2])]
    for i in range(2,n):
        dp.append(max(dp[i-1], dp[i-2]+arr[i]))
    return dp[n-1]

arr = [5,5,10,100,10,5,10] * 10
print(findMaxSum(arr))

