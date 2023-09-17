from collections import deque
# def rob(root):
#     pre, cur = 0, 0
#     q = deque([root])
#     while q:
#         node = q.popleft()
#         pre, cur = cur, max(pre+node.val, cur)
#         if node.left: q.append(node.left)
#         if node.right: q.append(node.right)
#     return cur

# def rob(root):
#     def dfs(root):
#         if not root:
#             return (0,0)
#         left_rob, left_not_rob = dfs(root.left)
#         right_rob, right_not_rob = dfs(root.right)
#         rob_this = root.val + left_not_rob + right_not_rob
#         not_rob_this = max(left_rob, left_not_rob) + max(right_rob, right_not_rob)
#         return (rob_this, not_rob_this)
    
#     return max(dfs(root))

def rob(root):
    def postorder(root):
        if not root:
            return (0,0)
        left_pre, left_cur = postorder(root.left)
        right_pre, right_cur = postorder(root.right)
        pre, cur = left_cur+right_cur, max(root.val+left_pre+right_pre, left_cur+right_cur)
        return pre, cur
    
    return postorder(root)[1]

