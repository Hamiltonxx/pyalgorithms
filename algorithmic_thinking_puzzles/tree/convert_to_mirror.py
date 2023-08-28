class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data 
        self.left = left 
        self.right = right 

def mirror(root):
    if root:
        mirror(root.left)
        mirror(root.right)
        root.left, root.right = root.right, root.left
    return root