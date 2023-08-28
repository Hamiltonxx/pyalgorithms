class SuffixTree:
    def __init__(self):
        self.root = {}

    def add_suffix(self, suffix):
        current_node = self.root 
        for char in suffix:
            if char not in current_node:
                current_node[char] = {}
            current_node = current_node[char]
        current_node['$'] = True

    def build_tree(self, text):
        # text += '$'  # Add a unique character to mark the end of the string
        for i in range(len(text)):
            self.add_suffix(text[i:])

    def search(self, pattern):
        current_node = self.root
        for char in pattern:
            if char not in current_node:
                return False
            current_node = current_node[char]
        return '$' in current_node
    
tree = SuffixTree()
tree.build_tree("banana")

print(tree.search("ana"))
print(tree.search("nan"))
print(tree.search("anana"))
print(tree.search("baa"))