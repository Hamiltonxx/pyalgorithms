# 7 6 4 5 3 2 
def maxProfit(prices):
    lowprice = prices[0]
    maxprofit = 0
    for x in prices[1:]:
        maxprofit = max(maxprofit, x-lowprice)
        lowprice = min(lowprice, x)
    return maxprofit

prices = [1]
print(maxProfit(prices))