class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 每个节点的三种状态: 0:无摄像头无覆盖; 1:有摄像头; 2:无摄像头有覆盖
# def minCamera(root):
#     res = 0
#     def fuck(root):
#         nonlocal res
#         if not root: return 0
#         r = fuck(root.left) | fuck(root.right)
#         res += r & 1
#         return [1,2,0,2][r]
#     r = fuck(root) & 1
#     return res + r


# Two bits information: 
# if the node has monitor[higher bit]; if the node is waiting for monitor[lower bit]
# 00 -> 01
# 01 -> 10
# 10 -> 00
class Solution:
    def minCameraCover(self, root):
        self.cnt = 0
        def postorder(root):
            if not root: return 0
            l = postorder(root.left)
            r = postorder(root.right)
            if l==0 and r==0: return 1
            elif l==1 or r==1: 
                self.cnt += 1
                return 2
            else: # l==2 or r==2
                return 0
        # if the root is waiting for parent's help, help itself
        help = postorder(root)==1
        return self.cnt + int(help)


