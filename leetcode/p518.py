# def change(amount, coins):
#     dp = [1,1] + [0] * amount
#     for i in range(2, amount+1):
#         for coin in coins:
#             if coin <= i:
#                 dp[i] += dp[i-coin]
#     return dp[amount]

def change(amount, coins):
    dp = [1] + [0]*amount
    for c in coins:
        for i in range(c, amount+1):
            dp[i] += dp[i-c]

    return dp[amount]

print(change(13,[3,5,7]))