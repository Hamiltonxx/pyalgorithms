from typing import Optional 

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class N(TreeNode):
    def __init__(self, x, left=None, right=None):
        TreeNode.__init__(x)
        self.left = left 
        self.right = right


# class Codec:
#     def serialize(self, root: Optional[TreeNode]) -> str:
#         """Encodes a tree to a single string.
#         """
#         def preorder(root):
#             if not root:
#                 return []
#             ans = [str(root.val)]
#             ans += preorder(root.left)
#             ans += preorder(root.right)
#             return ans
#         return ' '.join(preorder(root))       

#     def deserialize(self, data: str) -> Optional[TreeNode]:
#         """Decodes your encoded data to tree.
#         """
#         if not data:
#             return None 
#         vals = [int(x) for x in data.split()]
#         counter = 0
        
#         def buildTree(mn, mx):
#             nonlocal counter
#             if counter >= len(vals):
#                 return None
#             if (vals[counter] < mn or vals[counter] > mx):
#                 return None
            
#             node = TreeNode(vals[counter])
#             counter += 1
#             node.left = buildTree(mn, node.val)
#             node.right = buildTree(node.val, mx)
            
#             return node
        
#         return buildTree(float('-inf'),float('inf'))

# s = '{10:[5,15],5:[2,7],7:[6,"#"],15:["#",17]}'
# s = 'root=Node(10);root.left=Node(5);root.right=Node(15)'
# s = 'Node(10,Node(5),Node(15))'
# s = 'N(10,N(5),N(15))'
# d = eval(s)
