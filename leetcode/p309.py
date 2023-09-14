# def maxProfit(prices):
#     hold, sold, rest = -prices[0], 0, 0
#     for price in prices[1:]:
#         hold = max(hold, rest - price)
#         sold = hold + price
#         rest = max(rest, sold)
#     return max(sold, rest)

# def maxProfit(prices):
#     n = len(prices)
#     hold, sold, rest = [float('-inf')]*n, [0]*n, [0]*n
#     for i in range(1,n):
#         hold[i] = max(hold[i-1], rest[i-1]-prices[i])
#         sold[i] = hold[i-1] + prices[i]
#         rest[i] = max(rest[i-1], sold[i-1])
#     print(hold)
#     print(sold)
#     print(rest)
#     return max(sold[-1], rest[-1])

def maxProfit(prices):
    sold, hold, cool = 0, -prices[0], 0
    for p in prices[1:]:
        sold, hold, cool = hold+p, max(hold, cool-p), max(cool, sold)
    return max(sold, hold, cool)


print(maxProfit([1,2,3,0,2]))
print(maxProfit([1]))
    