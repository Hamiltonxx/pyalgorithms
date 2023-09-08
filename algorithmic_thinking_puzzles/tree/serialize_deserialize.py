# serialize and deserialize Binary Trees
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        return f'TreeNode({self.val})'
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return f'Node({self.val})'

# 把树序列化成字符串，再把字符串反序列化成树
#        10
#       /  \
#      5    15
#          /  \
#         12  17

# root = Node(10,Node(5),Node(15,Node(12),Node(17)))
root = Node(10,Node(5,Node(2),Node(7,Node(6))),Node(15,right=Node(17)))
# 解法一: BFS
from collections import deque
def serialize(root):
    res = []
    q = deque([root])
    while q:
        node = q.popleft()
        if node:
            q.append(node.left)
            q.append(node.right)
            res.append(str(node.val))
        else:
            res.append('#')
    return ','.join(res)

print(serialize(root))

def deserialize(data):
    nodes = data.split(',')
    root = Node(int(nodes[0]))
    i = 1
    q = deque([root])
    while q:
        node = q.popleft()
        if nodes[i] == '#':
            node.left = None
        else:
            t = TreeNode(int(nodes[i]))
            node.left = t
            q.append(t)
        i += 1 
        if nodes[i] == '#':
            node.right = None
        else:
            t = TreeNode(int(nodes[i]))
            node.right = t 
            q.append(t)
        i += 1
    return root


# post-order
def serialize_postorder(root):
    res = []  
    def postorder(root):
        if root:
            postorder(root.left)
            postorder(root.right)
            res.append(str(root.val))
        else:
            res.append('#')
    postorder(root)
    return ' '.join(res)

root = None
ser = serialize_postorder(root)
print(ser)

def deserialize(data):
    nodes = data.split()
    def postorder(nodes):
        if nodes[-1] == '#':
            nodes.pop()
            return None
        root = TreeNode(int(nodes.pop()))
        root.right = postorder(nodes)
        root.left = postorder(nodes)
        return root
    return postorder(nodes)

print(deserialize(ser))



