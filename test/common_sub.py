class Node:
    def __init__(self, start=None, end=None):
        self.start = start  # Start index of the substring
        self.end = end  # End index of the substring
        self.children = {}


def build_suffix_tree(strings):
    root = Node()
    for idx, string in enumerate(strings):
        string += '$'  # Add a unique character as a string terminator
        for i in range(len(string)):
            current_node = root
            j = i
            while j < len(string):
                char = string[j]
                if char not in current_node.children:
                    current_node.children[char] = Node(j)
                    break
                else:
                    child_node = current_node.children[char]
                    k = child_node.start
                    while k <= child_node.end and string[k] == string[j]:
                        k += 1
                        j += 1
                    if k <= child_node.end:
                        # Split the edge
                        current_node.children[char] = Node(child_node.start, k - 1)
                        new_node = Node(k, child_node.end)
                        new_node.children[string[k]] = child_node
                        current_node.children[char].children[string[k]] = new_node
                    else:
                        current_node = child_node

    return root


def find_lcs_suffix_tree(strings):
    def find_lcs_length(node, depth):
        if len(node.children) < len(strings):
            return 0
        lcs_length = 0
        for child in node.children.values():
            lcs_length = max(lcs_length, find_lcs_length(child, depth + 1))
        if depth > 0:
            lcs_length = max(lcs_length, node.end - node.start + 1)
        return lcs_length

    suffix_tree = build_suffix_tree(strings)
    lcs_length = find_lcs_length(suffix_tree, 0)
    return lcs_length


# Test example
strings = ["banana", "cabana"]
lcs_length = find_lcs_suffix_tree(strings)
print("Longest Common Substring Length:", lcs_length)