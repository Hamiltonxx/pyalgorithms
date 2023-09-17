class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def subtreeWithDeepest(root):
    def dfs(root):
        if not root: return 0, None 
        dl, left = dfs(root.left)
        dr, right = dfs(root.right)
        if dl > dr:
            return dl+1, left
        if dl < dr:
            return dr+1, right
        return dl+1, root
    
    return dfs(root)[1]