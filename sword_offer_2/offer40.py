import heapq 

arr = [3,2,1]
heapq.heapify(arr)
x = heapq.heappop(arr)

print(x)