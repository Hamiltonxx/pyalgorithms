def combinationSum4(nums, target):
    dp = [0] * (target+1)
    dp[0] = 1
    for j in range(target+1):
        for num in nums:
            if j >= num:
                dp[j] += dp[j-num]
    return dp[target]