def find_longest_common_substring(strings):
    def build_suffix_tree(strings):
        root = {}
        for i, string in enumerate(strings):
            node = root
            for char in string:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['$'] = i  # 使用字符串索引作为结束标记
        return root

    def find_lcs_length(node, depth, count):
        if '$' in node:
            count[node['$']] += 1
        lcs_length = 0
        for child in node.values():
            lcs_length = max(lcs_length, find_lcs_length(child, depth + 1, count))
        if count == [len(strings)] * len(strings):
            lcs_length = max(lcs_length, depth)
        if '$' in node:
            count[node['$']] -= 1
        return lcs_length

    suffix_tree = build_suffix_tree(strings)
    lcs_length = find_lcs_length(suffix_tree, 0, [0] * len(strings))
    return lcs_length


# 测试示例
strings = ["banana", "cabana"]
lcs_length = find_longest_common_substring(strings)
print("Longest Common Substring Length:", lcs_length)