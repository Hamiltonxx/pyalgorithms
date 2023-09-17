# def insert(intervals, newInterval):
#     ans = []
#     for interval in intervals:
#         if interval[1] < newInterval[0]:
#             ans.append(interval)
#         elif interval[0] > newInterval[1]:
#             ans.append(newInterval)
#             newInterval = interval
#         else:
#             newInterval = [
#                 min(interval[0], newInterval[0]),
#                 max(interval[1], newInterval[1])
#             ]
#     ans.append(newInterval)
#     return ans

import bisect
# def insert(intervals, newInterval):
#     bisect.insort(intervals, newInterval)
#     ans = intervals[:1]
#     for x in intervals[1:]:
#         if ans[-1][1] >= x[0]:
#             ans[-1][1] = max(ans[-1][1], x[1])
#         else:
#             ans.append(x)
#     return ans

def insert(intervals, newInterval):
    si = bisect.bisect_left(intervals, newInterval[0], key=lambda x:x[1])
    ei = bisect.bisect_right(intervals, newInterval[1], key=lambda x:x[0])

    start = min(intervals[si][0], newInterval[0]) if si<len(intervals) else newInterval[0]
    end = max(intervals[ei-1][1], newInterval[1]) if ei>0 else newInterval[1]

    return intervals[:si] + [[start,end]] + intervals[ei:]