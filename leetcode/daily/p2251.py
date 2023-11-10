# from itertools import accumulate
from bisect import bisect_left, bisect_right
def fullBloomFlowers(flowers, people):
    start = sorted(s for s,e in flowers)
    end = sorted(e for s,e in flowers)
    return [bisect_right(start, p) - bisect_left(end, p) for p in people]

flowers = [[1,10],[3,3]]
people = [3,3,2]
flowers = [[1,6],[3,7],[9,12],[4,13]]
people = [2,3,7,11]
# flowers = [[21,34],[17,37],[23,43],[17,46],[37,41],[44,45],[32,45]]
# people = [31,41,10,12]
print(fullBloomFlowers(flowers, people))

