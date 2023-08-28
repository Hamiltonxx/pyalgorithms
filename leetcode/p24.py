class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next 

def swapPairs(head):
    dummy = t = ListNode(next=head)
    while t.next and t.next.next:
        first = t.next
        second = first.next
        second.next = first
        first.next = second.next
        t.next = second
        t = first
    return dummy.next 
        
