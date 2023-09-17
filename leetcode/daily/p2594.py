import math
import bisect
def repairCars(ranks, cars):
    # arr = range(cars * cars * max(ranks))
    # f = lambda t: sum(math.isqrt(t/r) for r in ranks)
    return bisect.bisect_left(range(cars * cars * max(ranks)), cars, key=lambda t: sum(math.isqrt(t/r) for r in ranks))
