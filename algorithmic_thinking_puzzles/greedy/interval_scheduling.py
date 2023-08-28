# 区间调度问题
# S = {(start_i,end_i)}, 1<=i<=n
# Find a maximum subset S' that no pair of intervals in S' overlaps.
intervals = [(1,4),(3,6),(2,8),(5,9),(7,10),(9,12)]

def interval_scheduling(intervals): # -> maximum subset
    intervals.sort(key=lambda x:x[1])
    subset = intervals[:1]
    if len(intervals)==1:
        return subset
    for interval in intervals[1:]:
        if interval[0]>=subset[-1][1]:
            subset.append(interval)
    return subset

# def interval_scheduling(intervals):
#     intervals.sort(key=lambda x: x[1]) # 根据结束时间排序，优先选择结束时间更早的区间
#     S = []
#     for interval in intervals:
#         if not S or interval[0] >= S[-1][1]: # 当前区间的开始时间晚于最后一个区间的结束时间
#             S.append(interval)
#     return S 

max_subset = interval_scheduling(intervals)
print(max_subset)

# 区间染色问题 interval coloring 也叫区间划分问题 interval partitioning
# 找到一种最小颜色方案，使得任意两个重叠的区间不具有相同的颜色。
# 把区间划分为多个子集，使得每个子集中的区间互不相交
def interval_partition(intervals):
    intervals.sort(key=lambda x:x[1])
    partitions = []

    for interval in intervals:
        for part in partitions:
            if interval[0] >= part[-1][1]:
                part.append(interval)
                break
        else:
            partitions.append([interval])

    return partitions

# def interval_partition(intervals):
#     intervals.sort(key=lambda x:x[1])
#     partitions = []

#     for interval in intervals:
#         # Find a partition with the earliest end time that 
#         # doesnot overlap with the current interval
#         found_partition = False
#         for partition in partitions:
#             if interval[0] >= partition[-1][1]:
#                 partition.append(interval)
#                 found_partition = True 
#                 break
        
#         if not found_partition:
#             partitions.append([interval])

#     return partitions
