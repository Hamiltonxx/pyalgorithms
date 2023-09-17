import heapq
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    dummy = ListNode()
    head = dummy
    heap = [(x.val,x) for x in lists]
    heapq.heapify(heap)
    while heap:
        node = heapq.heappop(heap)
        head.next = node
        if node.next:
            heapq.heappush(heap, (node.next.val, node.next))
        head = node
    return dummy.next


