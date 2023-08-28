class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# def reverseKGroup(head,k):
#     dummy = everyk = ListNode(next=head)
#     stack = []
#     cnt = 0
#     while everyk.next:
#         t = everyk
#         while t.next:
#             if cnt<k:
#                 stack.append(t.next)
#                 t = t.next
#                 cnt += 1
#             else:
#                 for i in range(k-1,1,-1):
#                     stack[i].next = stack[i-1]
#                 everyk.next = stack[-1]
#                 everyk = stack[0]
            
#                 cnt = 0
#                 stack.clear()
#                 break 
#     return dummy.next

head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6,ListNode(7)))))))
k = 2

def reverseKGroup(head,k):
    dummy = t = ListNode(next=head)
    stack = []
    while t.next:
        stack.clear()
        tmp = t
        for i in range(k):
            if tmp.next:
                stack.append(tmp.next)
                tmp = tmp.next
            else:
                break
        if len(stack) == k:
            stack[0].next = stack[-1].next
            for j in range(1,k):
                stack[j].next = stack[j-1]
            t.next = stack[-1]
            t = stack[0]
        else:
            break
    return dummy.next

h = reverseKGroup(head,k)
# print(h.val)
# print(h.next.val)
# print(h.next.next.val)
print(h.next.next.val)   