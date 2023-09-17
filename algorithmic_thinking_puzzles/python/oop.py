class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# class ListNode:
#     def __init__(self, **kwargs):
#         for k,v in kwargs.items():
#             setattr(self, k, v)

node = ListNode(3)
setattr(node, 'visited', True)
print(node.val)
print(node.visited)

node2 = ListNode(2)
print(hasattr(node2, 'visited'))
print(hasattr(node, 'visited'))


