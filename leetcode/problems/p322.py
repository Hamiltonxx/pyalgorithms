# def coinChange(coins, amount):
#     dp = [0] + [float('inf')] * amount 
#     for coin in coins:
#         for i in range(coin, amount+1):
#             dp[i] = min(dp[i], dp[i-coin]+1)
#     return dp[amount]

# 完全背包
def coinChange(coins, amount):
    dp = [float('inf')] * (amount+1)
    dp[0] = 0
    for coin in coins:
        for j in range(coin, amount+1):
            dp[j] = min(dp[j], dp[j-coin]+1)
    return dp[amount]