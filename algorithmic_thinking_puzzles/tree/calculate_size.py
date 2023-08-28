class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data 
        self.left = left 
        self.right = right 

def calculate_size(root):
    if not root:
        return 0
    return calculate_size(root.left)+calculate_size(root.right)+1