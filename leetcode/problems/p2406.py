import random
# import heapq
# def minGroup(intervals):
#     intervals.sort()
#     hp = [intervals[0][1]] # 记录每组的结束时间
#     for s,e in intervals[1:]:
#         if hp[0] < s: # 和最早结束的分一组
#             heapq.heappop(hp)
#         heapq.heappush(hp, e)
#     return len(hp)

from collections import defaultdict
def minGroup(intervals):
    d = defaultdict(int)
    for l,r in intervals:
        d[l] += 1
        d[r+1] -= 1
    overlaps = res = 0
    for _,v in sorted(d.items()):
        overlaps += v
        res = max(res, overlaps)
    return res

intervals = []
for i in range(10):
    s = random.randrange(1,15)
    e = s + random.randrange(1,10)
    if [s,e] not in intervals:
        intervals.append([s,e])

print(intervals)
print(minGroup(intervals))