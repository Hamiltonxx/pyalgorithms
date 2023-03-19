# Inorder:
# 1.left subtree, 2.root, 3.right subtree
# Preorder:
# 1.root, 2.left subtree, 3.right subtree
# Postorder:
# 1.left subtree, 2.right subtree, 3.root

class Node:
    def __init__(self, data):
        self.left = None 
        self.right = None 
        self.val = data 

def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val)
        printInorder(root.right)

def printPreorder(root):
    if root:
        print(root.val)
        printPreorder(root.left)
        printPreorder(root.right)

def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Inorder:")
    printInorder(root)
    print("Preorder")
    printPreorder(root)
    print("Postorder")
    printPostorder(root)