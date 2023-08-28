class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data 
        self.left = left 
        self.right = right 


def preorder(root): # 先序，先root
    if not root:
        return []
    result = [root.data]
    result.extend(preorder(root.left))
    result.extend(preorder(root.right))
    return result
    
def preorder_iterative(root):
    if not root:
        return []
    stack = [root]
    result = []
    while stack:
        node = stack.pop()
        result.append(node.data)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result 

def inorder(root): # 中序，中root
    if not root:
        return []
    result = []
    result.extend(inorder(root.left))
    result.append(root.data)
    result.extend(inorder(root.right))
    return result 

def inorder_iterative(root):
    if not root:
        return []
    stack = []
    result = []
    node = root 
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            result.append(node.data)
            node = node.right
    return result

def postorder(root): # 后序，后root
    if not root:
        return []
    result = []
    result.extend(postorder(root.left))
    result.extend(postorder(root.right))
    result.append(root.data)
    return result 

def postorder_iterative(root):
    if not root:
        return []
    stack = [root]
    result = []
    while stack:
        node = stack.pop()
        result.append(node.data)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return result[::-1]