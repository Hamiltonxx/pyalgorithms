import bisect

def maximumJumps(nums, target):
    n = len(nums)
    jump = [(0,0)] # (跳的次数，下标)
    for i in range(1,n):
        for p in jump[::-1]:
            if abs(nums[p[1]]-nums[i]) <= target:
                # jump.insort((p[0]+1, i))
                bisect.insort(jump, (p[0]+1, i))
                break
                
    for p in jump:
        if p[1] == n-1:
            return p[0]
    return -1

nums = [1,3,6,4,1,2]
target = 2
print(maximumJumps(nums,target))