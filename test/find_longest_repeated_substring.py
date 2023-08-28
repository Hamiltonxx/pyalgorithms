class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.children = {}


def build_suffix_tree(string):
    root = Node(None, None)
    n = len(string)

    for i in range(n):
        suffix = string[i:]
        curr_node = root

        for char in suffix:
            if char not in curr_node.children:
                curr_node.children[char] = Node(i, None)
            curr_node = curr_node.children[char]

        curr_node.end = i

    return root


def find_longest_repeated_substring(string):
    def dfs(node, depth):
        nonlocal longest_substring

        if len(node.children) > 1 and depth > len(longest_substring):
            start = node.start
            end = node.end
            longest_substring = string[start:end+1]

        for child in node.children.values():
            dfs(child, depth + 1)

    suffix_tree = build_suffix_tree(string)
    longest_substring = ''
    dfs(suffix_tree, 0)

    return longest_substring


# 测试示例
text = "banana"
result = find_longest_repeated_substring(text)
print("Longest repeated substring:", result)