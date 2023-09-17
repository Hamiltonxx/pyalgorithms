# def goodNodes(root):
#     cnt = 1
#     stack = [root]
#     while stack:
#         node = stack.pop()
#         if node.left:
#             stack.append(node.left)
#             if node.val >= node.left.val:
#                 cnt += 1
#         if node.right:
#             stack.append(node.right)
#             if node.val >= node.right.val:
#                 cnt += 1
#     return cnt

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# node = TreeNode(1)
# setattr(node,'father','hello')
# print(node.val)


# def goodNodes(root, mx):
#     return int(root.val>=mx) + \
#            goodNodes(root.left, max(mx, root.val)) + \
#            goodNodes(root.right, max(mx, root.val)) if root else 0

def goodNodes(root):
    cnt = 0
    stack = [(root,float('-inf'))]
    while stack:
        node, mx = stack.pop()
        if node.val >= mx:
            mx = node.val
            cnt += 1
        if node.left:
            stack.append((node.left, mx))
        if node.right:
            stack.append((node.right, mx))
    return cnt
            
