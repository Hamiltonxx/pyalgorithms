class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minCamera(root):
    res = 0
    def fuck(root):
        nonlocal res
        if root == None: return 0
        r = fuck(root.left) | fuck(root.right)
        res += r & 1
        return [1,2,0,2][r]
    r = fuck(root) & 1
    return res + r