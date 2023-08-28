import heapq
def findKthLargest(nums, k):
    h = [-x for x in nums]
    heapq.heapify(h)
    return -heapq.nsmallest(k,h)[-1]

def findKthLargest2(nums, k):
    h = nums[:k]
    heapq.heapify(h)

    for x in nums[k:]:
        if x>h[0]:
            heapq.heappop(h)
            heapq.heappush(h, x)

    return h[0]


nums = [3,2,1,5,6,4]
k = 2
print(findKthLargest(nums,k))