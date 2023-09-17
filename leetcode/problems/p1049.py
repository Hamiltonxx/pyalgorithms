stones = [31,26,33,21,40]
def lastStoneWeightII(nums):
    sm = sum(nums)
    target = sm // 2
    dp = [False] * (target+1)
    dp[0] = True
    for num in nums:
        for j in range(target, num-1, -1):
            dp[j] = dp[j] or dp[j-num]
    while target:
        if dp[target]: break 
        target -= 1
    return sm - 2*target

print(lastStoneWeightII(stones))
print(lastStoneWeightII([91]))


def last_stone_weight(nums):
    sm = sum(nums)
    target = sm // 2
    dp = [0] * (target+1)
    for num in nums:
        for j in range(target, num-1, -1):
            dp[j] = max(dp[j], dp[j-num]+num)
    return sm - 2 * dp[target]

stones = [91]
print(last_stone_weight(stones))

