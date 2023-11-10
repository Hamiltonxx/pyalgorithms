def filterRestaurants(restaurants, veganFriendly, maxPrice, maxDistance):
    func = lambda x: x[2]>=veganFriendly and x[3]<=maxPrice and x[4]<=maxDistance
    filtered = list(filter(func, restaurants))
    filtered.sort(key=lambda x:(-x[1],-x[0]))
    return [r[0] for r in filtered]