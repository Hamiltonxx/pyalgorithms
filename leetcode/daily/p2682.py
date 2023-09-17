def circularGameLosers(n,k):
    winner = set()
    i = 1
    current = 0
    while current not in winner:
        winner.add(current)
        current = (current + i*k) % n
        i += 1
    loser = [j+1 for j in range(n) if j not in winner]
    return loser

print(circularGameLosers(5,2))