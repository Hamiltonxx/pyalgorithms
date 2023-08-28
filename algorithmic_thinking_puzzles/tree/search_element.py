class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data 
        self.left = left 
        self.right = right 

def search_element(root,elm):
    left = search_element(root.left)
    right = search_element(root.right)
    return elm in (root.data, left, right)
