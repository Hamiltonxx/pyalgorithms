# 15 6 3 7 2 9 4
# 15 6 3 7 8 9 4

# def maxProfit(prices):
#     n = len(prices)
#     profit = 0
#     for i in range(1,n):
#         if prices[i] > prices[i-1]:
#             profit += prices[i] - prices[i-1]
#     return profit

# prices = [15,6,3,7,2,9,4]
# print(maxProfit(prices))

def max_profit(prices):
    profit = 0
    for x,y in zip(prices[:-1],prices[1:]):
        if y > x:
            profit += y - x
    return profit