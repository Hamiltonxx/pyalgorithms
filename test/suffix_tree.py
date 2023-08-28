# class Node:
#     def __init__(self):
#         self.children = {}  # 子节点字典


# class SuffixTree:
#     def __init__(self, string):
#         self.string = string
#         self.root = Node()  # 初始化根节点
#         self.build_suffix_tree()

#     def build_suffix_tree(self):
#         n = len(self.string)
#         for i in range(n):
#             suffix = self.string[i:]
#             curr_node = self.root
#             for char in suffix:
#                 if char not in curr_node.children:
#                     curr_node.children[char] = Node()
#                 curr_node = curr_node.children[char]

#     def traverse(self, node, substring):
#         if not node.children:
#             print(substring)
#             return

#         for char, child in node.children.items():
#             self.traverse(child, substring + char)


# # 测试示例
# suffix_tree = SuffixTree("banana")
# suffix_tree.traverse(suffix_tree.root, "")



"""http://goo-apple.appspot.com/article/2e8d3c6a-2c38-48b9-96c6-240b4ded253a"""
class Node:
        def __init__(self, start, substr):
                self.start = start
                self.substr = substr
                self.branches = {}
              
def insert_into_tree(subroot, suffix, start):
        prefix_len = len(subroot.substr)
        new_suffix = str(suffix[prefix_len:])
        if(len(subroot.branches) == 0):
                left_child = Node(subroot.start, "")
                right_child = Node(start, new_suffix)
                subroot.branches[""] = left_child
                subroot.branches[new_suffix] = right_child
        else:
                for (substr, node) in subroot.branches.items():
                        if len(substr) > 0 and new_suffix.startswith(substr):
                                insert_into_tree(node, new_suffix, start)
                                break
                else:
                        new_child = Node(start, new_suffix)
                        subroot.branches[new_suffix] = new_child
              
def build_suffix_tree(t_str):
        len_str = len(t_str)
        i = len_str - 1
        root = Node(len_str, "")
        while i >= 0:
                insert_into_tree(root, str(t_str[i:]), i)
                i -= 1
        return root
              
def display_all_suffix(subroot, suffix_s_prefix, level = 0):
        if len(subroot.branches) == 0:
                print(suffix_s_prefix, level)
                return
        for (substr, node) in subroot.branches.items():
                display_all_suffix(node, suffix_s_prefix + substr, level + 1)
              
root = build_suffix_tree("BCABC")
display_all_suffix(root, "")