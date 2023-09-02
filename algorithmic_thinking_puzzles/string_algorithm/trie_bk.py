# Trie(前缀树或字典树),是一种用于高效存储和搜索字符串的树形数据结构。
# 每个节点代表一个字母，从根节点到叶子节点的路径构成一个字符串。
# Trie的主要特点是能够在O(m)的时间复杂度内进行字符串的插入、搜索和删除操作。
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root 
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True 

    def search(self, word):
        node = self.root 
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
    
    def starts_with(self, prefix):
        node = self.root 
        for char in prefix:
            if char not in node.children:
                return False 
            node = node.children[char]
        return True 

# 创建 Trie 实例
trie = Trie()

# 插入单词
trie.insert("apple")
trie.insert("banana")
trie.insert("orange")

# 搜索单词
print(trie.search("apple"))  # 输出: True
print(trie.search("grape"))  # 输出: False

# 前缀搜索
print(trie.starts_with("app"))  # 输出: True
print(trie.starts_with("pear"))  # 输出: False 

## 自己动手写
def make_trie(words):
    trie = {}
    for word in words:
        head = trie 
        for char in word:
            head = head.setdefault(char, {})
        head["_end"] = "_end"
    return trie

def in_trie(trie, word):
    head = trie 
    for char in word:
        if char not in head:
            return False
        head = head[char]
    return "_end" in head 