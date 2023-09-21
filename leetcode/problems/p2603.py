from collections import defaultdict
def collectTheCoins(coins, edges):
    if not edges:
        return 0
    n, d = len(coins), defaultdict(set)
    for i,j in edges:
        d[i].add(j)
        d[j].add(i)
    leaves = [i for i in d if len(d[i])==1]

    for u in leaves:
        while len(d[u])==1 and coins[u]==0:
            v = d[u].pop()
            del d[u]
            d[v].remove(u)
            u = v

    for _ in range(2):
        leaves = [i for i in d if len(d[i])==1]
        for u in leaves:
            v = d[u].pop()
            del d[u]
            d[v].remove(u)
            if len(d) < 2:
                return 0
            
    return 2*(len(d)-1)