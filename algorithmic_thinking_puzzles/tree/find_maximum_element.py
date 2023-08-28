class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data 
        self.left = left 
        self.right = right 

def find_max(root):
    if not root:
        return float('-inf')
    left_max = find_max(root.left)
    right_max = find_max(root.right)
    return max(root.data, left_max, right_max)

def find_max_iterative(root):
    if not root:
        return float('-inf')
    mx = float('-inf')
    stack = [root]
    while stack:
        node = stack.pop()
        if node.data > mx:
            mx = node.data
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return mx 