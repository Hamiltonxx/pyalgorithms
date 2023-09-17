# 区间调度
# Find a maximum subset S' that no pair of intervals in S' overlaps.
intervals = [(1,4),(3,6),(2,8),(5,9),(7,10),(9,12)]

def interval_schedule(intervals): # -> maximum subset
    intervals.sort(key=lambda x:x[1])
    mxset = intervals[:1]
    for interval in intervals[1:]:
        if interval[0] > mxset[-1][1]:
            mxset.append(interval)
    return mxset

# 区间划分
# 把区间划分为多个子集，使得每个子集中的区间互不相交
# 区间染色问题 interval coloring 也叫区间划分问题 interval partitioning
# 找到一种最小颜色方案，使得任意两个重叠的区间不具有相同的颜色。
import heapq
def interval_partition(intervals): # -> minimum groups number
    intervals.sort()
    hp = [intervals[0][1]]
    for s,e in intervals[1:]:
        if hp[0] < s:
            heapq.heappop(hp)
        heapq.heappush(hp, e)
    return len(hp)

# 区间合并
def interval_merge(intervals): # -> merged intervals
    intervals.sort()
    ans = intervals[:1]
    for s,e in intervals[1:]:
        if s <= ans[-1][1]:
            ans[-1][1] = max(ans[-1][2], e)
        else:
            ans.append([s,e])
    return ans

# 差分数组
# 原始数组a[x]  0  2  5  4  9  7  10  0
# 差分数组d[x]     2  3  -1 5  -2 3   -10
# 表示数组的变化，一般用来数据区间修改操作。
# 当a[1:5]都+3，则d[1]+3,d[2:5]不变,d[5]-3
# 差分数组d[x]     5  3  -1 5  -5 3   -10
# 当对一数组的某一区间进行增减某值时，其差分数组对应的区间左端点的值会同步变化，右端点的后一值会相反变化
nums = [0, 2, 5, 4, 9, 7, 10, 0]
diff = [0] + [y-x for x,y in zip(nums[:-1],nums[1:])]
print(diff)
# 通过差分数组得到原数组
res = diff[:1]
for d in diff[1:]:
    res.append(res[-1]+d)
print(res)
# 给区间[i,j] +/- val
i,j, val = 2,5, 3
diff[i] += val
if j < len(diff) - 1:
    diff[j+1] -= val

