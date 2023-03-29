# Min Heap: Each parent node is less than or equal to its child node.
# Max Heap: Each parent node is greater than or equal to its child node.
# useful in priority queue
# heapify  heappush  heappop  heapreplace

import heapq 

H = [21,1,45,78,3,5]
heapq.heapify(H)
print(H)

heapq.heappush(H,8)
print(H)

heapq.heappop(H)
print(H)

heapq.heapreplace(H,6)
print(H)

# usage: 
#import heapq
#heapq.heapify(lst)
#heapq.heappush(lst,ele)
#x = heapq.heappop(lst)
#x = heapq.heappushpop(lst,ele)
#x = heapq.heapreplace(lst,ele)
#heapq.nlargest(n,lst)
#heapq.nsmallest(n,lst)
lst = [5,12,9,4,8]
print("init lst:",lst)
heapq.heapify(lst)
print(lst)
heapq.heappush(lst,6)
print(lst)
x = heapq.heappop(lst)
print(x)
print(lst)
y = heapq.heappushpop(lst,3)
print(y)
print(lst)
z = heapq.heapreplace(lst,7)
print(z)
print(lst)
print(heapq.nlargest(2,lst))
print(heapq.nsmallest(3,lst))