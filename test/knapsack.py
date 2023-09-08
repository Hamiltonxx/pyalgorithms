weight, value, capacity = [1, 3, 4], [15, 20, 30], 4
def knapsack01(weight, value, capacity):
    n = len(weight)
    dp = [[0]*(capacity+1) for _ in range(n)]
    for j in range(weight[0], capacity+1):
        dp[0][j] = value[0]
    for i in range(1,n):
        for j in range(1,capacity+1):
            if weight[i] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]] + value[i])
    return dp[-1][-1]

print(knapsack01(weight, value, capacity))

# subset sum problem
nums, target = [3,2,4,19,3,7,13,10,6,11], 17
def exist_subset_sum(nums, target):
    # dp[i][j]定义为前i个数和为j是否存在
    # dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
    n = len(nums)
    dp = [[False]*(target+1) for _ in range(n)]
    for i in range(n):
        dp[i][0] = True
    for i in range(n):
        for j in range(1,target+1):
            if nums[i] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
    return dp[-1][-1]

print(exist_subset_sum(nums, target))