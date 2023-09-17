class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# def partition(head, x):
#     dummy = t = ListNode(next=head)
    
#     small = st = ListNode()
#     large = lt = ListNode()

#     while t.next:
#         if t.next.val < x:
#             st.next = t.next
#             st = st.next
#         else:
#             lt.next = t.next
#             lt = lt.next
#         t = t.next

#     if small.next:
#         dummy.next = small.next
#         st.next = large.next
#     else:
#         dummy.next = large.next

#     return dummy.next

def partition(head, x):
    dummy = t = ListNode(next=head)
    large = lh = ListNode()
    while t.next:
        if t.next.val < x:
            t = t.next
        else:
            lh.next = t.next
            lh = lh.next
            t.next = t.next.next
    t.next = large.next
    lh.next = None
    return dummy.next


    
head = ListNode(1,ListNode(4,ListNode(3,ListNode(2,ListNode(5,ListNode(2))))))
x = 3
ans = partition(head,x)
print(ans.next.next.val)