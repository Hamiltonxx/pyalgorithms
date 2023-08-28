def make_suffix_tree(string):
    tree = {}
    n = len(string)

    for i in range(n):
        suffix = string[i:]
        head = tree
        for char in suffix:
            head = head.setdefault(char, {})

    return tree

def traverse_suffix_tree(tree, substring):
    if not tree:
        print(substring)
        return 
    
    for char, child in tree.items():
        traverse_suffix_tree(child, substring + char)

# 测试示例
suffix_tree = make_suffix_tree("tatat")
traverse_suffix_tree(suffix_tree, "")

def find_longest_repeated_substring(string):
    suffix_tree = make_suffix_tree(string)
    longest_substring = ''
    stack = [(suffix_tree, '')]

    while stack:
        node, substring = stack.pop()

        # 检查当前子串是否更长
        if len(substring) > len(longest_substring):
            longest_substring = substring

        # 将所有子节点加入栈中
        for child in node.values():
            stack.append((child, substring+child))

    return longest_substring

text = "banana"
print(find_longest_repeated_substring(text))