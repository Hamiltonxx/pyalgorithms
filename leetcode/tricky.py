# 小技巧

# 修改 TreeNode构造函数/参数, 用继承
class Node(TreeNode):
    def __init__(self, x, left=None, right=None):
        TreeNode.__init__(x)
        self.left = left 
        self.right = right 