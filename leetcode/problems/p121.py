# # 7 6 4 5 3 2 
# def maxProfit(prices):
#     lowprice = prices[0]
#     maxprofit = 0
#     for x in prices[1:]:
#         maxprofit = max(maxprofit, x-lowprice)
#         lowprice = min(lowprice, x)
#     return maxprofit

# prices = [1]
# print(maxProfit(prices))

prices = [7,1,5,3,6,4]
def max_profit(prices):
    cost, profit = 10000, 0
    for price in prices:
        cost = min(cost, price)  # 当前买股票的最小代价
        profit = max(profit, price-cost)  # 当前卖股票的最大获利
    
    return profit

print(max_profit(prices))