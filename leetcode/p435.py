def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x:x[1])
    cnt = 0
    end = -float('inf')

    for interval in intervals:
        if interval[0] >= end:
            end = interval[1]
        else:
            cnt += 1

    return cnt
    

