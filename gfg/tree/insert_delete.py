class Node:
    def __init__(self,data):
        self.data = data
        self.left = None 
        self.right = None 

def inorder(node):
    if not node:
        return 
    inorder(node.left)
    print(node.data, end=" ")
    inorder(node.right)

def insert(node,data):
    q = []
    q.append(node)

    # Do level order traversal until we find an empty place
    while q:
        temp = q[0]
        q.pop(0)

        if not temp.left:
            temp.left = Node(data)
            break 
        else:
            q.append(temp.left)

        if not temp.right:
            temp.right = Node(data)
            break 
        else:
            q.append(temp.right)

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    # root.left.right = Node(17)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)

    print("Inorder traversal before insertion: ",end=" ")
    inorder(root)

    data = 12
    insert(root,data)
    print()

    print("Inorder traversal after insertion: ",end=" ")
    inorder(root)