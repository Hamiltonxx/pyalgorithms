# making coin change
# output the minimum number of coins
coins = [1,5,10,20,25,50]
change = 40
# greedy在这里不适用。40=25+10+5，而解是40=20+20. 
# 这里应该用Dynamic Programming

# Fractional Knapsack problem
# Given items t1,t2...tn, weights w1,w2...wn, values v1,v2...vn
# Limit Wight C, maximize total benefit
def fractional_knapsack(weights, values, weight_limit):
    n = len(weights)
    ratios = [(values[i]/weights[i], i) for i in range(n)]
    ratios.sort(reverse=True)

    w = 0
    b = 0
    for ratio,idx in ratios:
        if w + weights[idx] <= weight_limit:
            b += values[idx]
            w += weights[idx]
        else:
            b += (weight_limit - w) / weights[idx] * values[idx]
            break
    
    return b
# 这里排序需要O(Nlog(N))的时间复杂度。
# 如果用最小堆，一个个取直到包满，那么时间复杂度是O(N+Clog(N)), C是选中数。
# There is a savings in runtime if C=O(N), otherwise there is no change in the complexity.

# 建基站问题
# 假设道路无限长，房子沿道路而建，基站能覆盖r公里的信号。求最小基站数
def min_towers(houses, r):
    houses.sort()
    towers = [-float('inf')]
    for x in houses:
        if x > towers[-1] + r:
            towers.append(x+r)
    # return towers[1:]
    return len(towers) - 1

houses = [2, 5, 10, 15, 20, 23, 30, 35, 40, 45, 50]
r = 7
print(min_towers(houses, r))