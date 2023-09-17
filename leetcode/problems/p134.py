def canCircuit(gas, cost):
    if sum(gas) < sum(cost): 
        return -1
    amount = 0
    ans = 0
    for idx, (g,c) in enumerate(zip(gas, cost)):
        amount += g - c 
        if amount < 0:
            amount = 0
            ans = idx + 1
    return ans

# gas = [1,2,3,4,5]
# cost = [3,4,5,1,2]
gas = [5,8,2,8]
cost = [6,5,6,6]   

print(canCircuit(gas,cost))
