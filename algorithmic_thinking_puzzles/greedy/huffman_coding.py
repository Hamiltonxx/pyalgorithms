import heapq 
from collections import Counter

# inputText = "this is an example for huffman encoding"
# frequencyCounter = Counter(inputText)
text = "aaabbcccdddd"
frequencyCounter = Counter(text)
print(frequencyCounter)

def huffman_encode(frequencyCounter):
    heap = [[freq, [sym, ""]] for sym,freq in frequencyCounter.items()]
    heapq.heapify(heap)
    while len(heap)>1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap,[lo[0]+hi[0]]+lo[1:]+hi[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]),p))

print(huffman_encode(frequencyCounter))