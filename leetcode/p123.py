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

def maxProfit(prices):
    buy1 = buy2 = float('inf')
    sell1 = sell2 = 0

    for price in prices:
        buy1 = min(buy1, price)
        sell1 = max(sell1, price-buy1)
        buy2 = min(buy2, price-sell1)
        sell2 = max(sell2, price-buy2)

    return sell2