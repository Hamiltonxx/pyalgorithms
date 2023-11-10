def earliestFullBloom(plantTime, growTime):
    prevPlant, ans = 0, 0
    for grow, plant in sorted(zip(growTime, plantTime), reverse=True):
        ans = max(ans, prevPlant+plant+grow)
        prevPlant += plant
    return ans