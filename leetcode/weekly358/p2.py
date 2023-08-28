import sys
sys.set_int_max_str_digits(0)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def doubleIt(head):
    num = []
    while head:
        num.append(str(head.val))
        head = head.next
    num = int("".join(num)) * 2
    dummy = head = ListNode()
    for x in str(num):
        head.next = ListNode(int(x))
        head = head.next
    return dummy.next

