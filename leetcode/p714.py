import random
def maxProfit(prices, fee):
    hold, sold = -prices[0], 0
    for price in prices[1:]:
        hold = max(hold, sold-price)
        sold = max(sold, hold + price - fee)
    return max(hold, sold)

# prices = [1, 3, 2, 8, 4, 9]
fee = 2
# prices = [1,3,7,5,10,3]
# fee = 3
prices = [random.randrange(1,20) for _ in range(10)]
print(prices)

print(maxProfit(prices, fee))