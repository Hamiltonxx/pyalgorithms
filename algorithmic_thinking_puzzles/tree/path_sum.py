class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data 
        self.left = left 
        self.right = right 

def max_path_sum(root):
    if not root:
        return 0
    left_sum = max_path_sum(root.left)
    right_sum = max_path_sum(root.right)
    return max(left_sum+root.data, root.data, right_sum+root.data)
