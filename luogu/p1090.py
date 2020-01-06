import heapq 

n = int(input())
a = list(map(int,input().split()))
heapq.heapify(a)

s = 0
while True:
    new = heapq.heappop(a) + heapq.heappop(a)
    s += new
    if not a:
        break
    heapq.heappush(a,new) 
print(s)