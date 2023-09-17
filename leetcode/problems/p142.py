class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def detectCycle(head):
    head.visited = True
    while head.next:
        if head.next.visited:
            return head.next
        head = head.next
