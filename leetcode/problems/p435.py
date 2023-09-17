# def eraseOverlapIntervals(intervals):
#     intervals.sort(key=lambda x:x[1])
#     cnt = 0
#     end = -float('inf')

#     for interval in intervals:
#         if interval[0] >= end:
#             end = interval[1]
#         else:
#             cnt += 1

#     return cnt



def interval_schedule(intervals):
    intervals.sort(key=lambda x:x[1])
    mxset = intervals[:1]
    for s,e in intervals[1:]:
        if s >= mxset[-1][1]:
            mxset.append([s,e])
    return mxset

# def eraseOverIntervals(intervals):
#     return len(intervals) - len(interval_schedule(intervals))

def eraseInterval(intervals):
    intervals.sort(key=lambda x:x[1])
    cnt = 0
    end = intervals[0][1]
    for s,e in intervals[1:]:
        if s >= end:
            end = e
        else:
            cnt += 1
    return cnt