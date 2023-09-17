# prices = [6,3,7,2,5,9,1,10]
prices = [3,3,5,0,0,3,1,4]
# prices = [1,4,2]

# def maxtwo(a,b,c):
#     (mx1,mn1) = (a,b) if a>=b else (b,a)
#     mx2 = max(mn1,c)
#     return mx1, mx2

# def maxProfit(prices):
#     n = len(prices)
#     # a,b = 0,0
#     mx = [0]
#     low = prices[0]
#     mxtmp = 0
#     for i in range(1,n):
#         if prices[i] > prices[i-1]:
#             mxtmp = prices[i] - low
#         else:
#             low = prices[i]
#             mx.append(mxtmp)
#             if len(mx)==3:
#                 mx.remove(min(mx))
#             # a,b = maxtwo(a,b,mxtmp)
#     # return a+b if mxtmp in [a,b] else sum(maxtwo(a,b,mxtmp))
#     # return maxtwo(a,b,mxtmp)
#     if mxtmp not in mx:
#         mx.append(mxtmp)
#         mx.remove(min(mx))
#     return sum(mx)

# print(maxProfit(prices))

# def maxProfit(prices):
#     buy1 = buy2 = float('inf')
#     sell1 = sell2 = 0

#     for price in prices:
#         buy1 = min(buy1, price)
#         sell1 = max(sell1, price-buy1)
#         buy2 = min(buy2, price-sell1)
#         sell2 = max(sell2, price-buy2)

#     return sell2

# def max_profit(prices):
#     cost = [100000] * 3
#     profit = [0] * 3

#     for price in prices:
#         for i in range(1,3):
#             cost[i] = min(cost[i], price-profit[i-1])
#             profit[i] = max(profit[i], price-cost[i])
#     return profit[2]

# prices = [3,3,5,0,0,3,1,4]
# print(max_profit(prices)) 

def maxProfit(prices):
    cost1 = cost2 = float('inf')
    profit1 = profit2 = 0
    # cost1: the minimum cost so far for the first transaction
    # profit1: the maximum profit so far for the first transaction
    # cost2: the minimum cost so far for the second transaction 
    # profit2: the maximum profit so far for the second transaction
    for price in prices:
        cost1 = min(cost1, price)
        profit1 = max(profit1, price-cost1)
        cost2 = min(cost2, price-profit1)
        profit2 = max(profit2, price-cost2)
    return profit2
