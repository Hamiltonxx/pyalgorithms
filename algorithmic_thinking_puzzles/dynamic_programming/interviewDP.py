## 1. Fibonacci [1,1,2,3,5,8]
def fibonacci(n):
    series = [1,1]
    while len(series) < n:
        series.append(series[-1] + series[-2])
    return series[-1]
# we do not need to store the entire sequence, just last two number
def fibonacci(n):
    previous, current = 1, 1
    for i in range(n-2): # or range(3,n+1)
        # next = current + previous
        # previous, current = current, next
        previous, current = current, previous + current
    return current
print(fibonacci(5))

## 2. Stock market strategy [2,5,1,3]
# Assume that you are allowed to own no more than 1 share at any time
import random 
prices = [random.randrange(1,20) for _ in range(8)]
print(prices)
# prices = [3, 10, 8, 2, 15, 5, 19, 10]
# A state machine
# today                  tomorrow
# cash     -- avoid ->   cash
#          \       /
#           \  buy
# cash &   / sell    \    cash &
# 1 share / -- hold ->\   1 share
def max_profit_fsm(prices):
    cash_no_share = 0
    cash_with_share = float('-inf')
    for price in prices:
        cash_no_share_cp, cash_with_share_cp = cash_no_share, cash_with_share
        cash_no_share = max(cash_no_share_cp, cash_with_share_cp + price)
        cash_with_share = max(cash_no_share_cp - price, cash_with_share_cp)
    return cash_no_share
print(max_profit_fsm(prices))
# def max_profit_fsm(prices):
#     cash_not_owning_share = 0
#     cash_owning_share = float('-inf')
#     for price in prices:
#         strategy_buy = cash_not_owning_share - price
#         strategy_hold = cash_owning_share
#         strategy_sell = cash_owning_share + price 
#         strategy_avoid = cash_not_owning_share
#         # Compute the new states
#         cash_owning_share = max(strategy_buy, strategy_hold)
#         cash_not_owning_share = max(strategy_sell, strategy_avoid)
#     return cash_not_owning_share
def max_profit_leetcode(prices):
    profit = 0
    for x,y in zip(prices[:-1], prices[1:]):
        if x < y:
            profit += -x + y 
    return profit
print(max_profit_leetcode(prices))
# Variation: limited investment budget
def max_profit_limit_budget(prices, budget):
    # cash0 表示没有股票， cash1表示有股票
    cash0 = budget
    cash1 = -float('inf')
    for price in prices:
        cash0cp, cash1cp = cash0, cash1
        cash0 = max(cash0cp, cash1cp+price)
        cash1 = max(cash0cp-price, cash1cp)
        if cash1 < 0: cash1 = -float('inf')
        # Add a high penalty to ensure we never choose this option.
    return cash0 - budget
budget = random.randrange(min(prices), prices[0])
# budget = random.randrange(min(prices))
print('budget',budget)
print(max_profit_limit_budget(prices, budget))
# 请掌握有限状态机，几乎所有的DP问题都能用这种方式解决
# Variation: limited number of transactions
# The stock can only be sold up to a certain number of times.
INF = float('inf')
def max_profit_limit_transactions_leetcode(prices, tx):
    cost = [INF] * (tx+1)
    profit = [0] * (tx+1)
    for price in prices:
        for i in range(1, tx+1):
            cost[i] = min(cost[i], price-profit[i-1])
            profit[i] = max(profit[i], price-cost[i])
    return profit[tx]

## 3. Change making 
