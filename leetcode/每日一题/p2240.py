def waysToBuy(total, cost1, cost2):
    cnt = 0
    (cost1,cost2) = (cost1,cost2) if cost1 > cost2 else (cost2,cost1)
    for i in range(total//cost1+1):
        cnt += (total - cost1 * i) // cost2 + 1
    return cnt
