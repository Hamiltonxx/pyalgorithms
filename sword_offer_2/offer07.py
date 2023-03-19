# rebuild tree by inorder and preorder traversal
# preorder=[3,9,20,15,7], inorder=[9,3,15,20,7]

class Node:
    def __init__(self, data):
        self.left = None 
        self.right = None 
        self.val = data 

def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None
    root = Node(preorder[0])
    index = inorder.index(preorder[0])
    root.left = buildTree(preorder[1:index+1], inorder[:index])
    root.right = buildTree(preorder[index+1:], inorder[index+1:])
    return root