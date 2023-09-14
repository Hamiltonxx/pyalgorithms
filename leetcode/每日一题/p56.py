# def merge(intervals):

#     intervals.sort(key=lambda x:x[0])
#     ans = intervals[:1]
#     for interval in intervals[1:]:
#         if interval[0] <= ans[-1][1]:
#             ans[-1] = [ans[-1][0], max(ans[-1][1],interval[1])]
#         else:
#             ans.append(interval)
#     return ans


# intervals = [[1,3],[2,6],[8,10],[15,18]]
# print(merge(intervals))

