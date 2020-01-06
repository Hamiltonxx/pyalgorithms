# 二叉树的节点
class Node:
    def __init__(self, data):
        self.left = None 
        self.right = None 
        self.val = data

# 创建根节点
root = Node(1)
''' 创建好根节点后的树 
        1 
      /   \ 
     None  None'''
root.left = Node(2)
root.right = Node(3)
''' 2 和 3 成为 1 的左右孩子 
           1 
         /   \ 
        2      3 
     /    \    /  \ 
   None None None None'''
root.left.left = Node(4)
'''4 成为 2 的左孩子 
           1 
       /       \ 
      2          3 
    /   \       /  \ 
   4    None  None  None 
  /  \ 
None None'''