# 后缀树的节点类
class Node:
    def __init__(self, start, end):
        self.start = start  # 后缀的起始索引
        self.end = end  # 后缀的结束索引
        self.children = {}  # 子节点的映射表

# 后缀树类
class SuffixTree:
    def __init__(self, text):
        self.root = Node(None, None)  # 根节点
        self.text = text  # 要构建后缀树的字符串
        self.construct_suffix_tree()  # 构建后缀树

    def construct_suffix_tree(self):
        n = len(self.text)

        # 逐个插入后缀到后缀树中
        for i in range(n):
            suffix = self.text[i:]  # 当前后缀
            current_node = self.root

            for char in suffix:
                # 如果当前字符不在当前节点的子节点中，则创建一个新的子节点
                if char not in current_node.children:
                    current_node.children[char] = Node(i, None)
                current_node = current_node.children[char]

            current_node.end = i  # 标记后缀的结束索引

    # 打印后缀树
    def print_suffix_tree(self, node=None, level=0):
        if node is None:
            node = self.root

        prefix = ""
        if node.start is not None and node.end is not None:
            prefix = self.text[node.start:node.end+1]

        print("  " * level + prefix)

        for child in node.children.values():
            self.print_suffix_tree(child, level + 1)

# 示例用法
text = "banana"
suffix_tree = SuffixTree(text)
suffix_tree.print_suffix_tree()