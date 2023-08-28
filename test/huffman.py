import heapq
from collections import defaultdict

# 定义节点类
class Node:
    def __init__(self, char, freq):
        self.char = char  # 字符
        self.freq = freq  # 频率
        self.left = None  # 左子节点
        self.right = None  # 右子节点

    # 定义比较方法，用于节点的优先级比较
    def __lt__(self, other):
        return self.freq < other.freq


# 统计字符频率
def get_char_frequency(text):
    frequency = defaultdict(int)
    for char in text:
        frequency[char] += 1
    return frequency


# 构建哈夫曼树
def build_huffman_tree(frequency):
    heap = []
    # 将每个字符及其频率作为一个节点加入最小堆
    for char, freq in frequency.items():
        node = Node(char, freq)
        heapq.heappush(heap, node)

    # 从最小堆中选择两个频率最低的节点，合并它们成为一个新节点，并将新节点放回最小堆中，直到堆中只剩下一个节点
    while len(heap) > 1:
        left_node = heapq.heappop(heap)
        right_node = heapq.heappop(heap)
        merged_node = Node(None, left_node.freq + right_node.freq)
        merged_node.left = left_node
        merged_node.right = right_node
        heapq.heappush(heap, merged_node)

    # 返回哈夫曼树的根节点
    return heap[0]


# 生成哈夫曼编码表
def generate_huffman_codes(root):
    codes = {}

    def traverse(node, code):
        if node.char is not None:
            codes[node.char] = code
            return
        traverse(node.left, code + '0')
        traverse(node.right, code + '1')

    traverse(root, '')
    return codes


# 使用哈夫曼编码压缩文本
def compress_text(text):
    frequency = get_char_frequency(text)
    root = build_huffman_tree(frequency)
    codes = generate_huffman_codes(root)
    
    compressed_text = ''
    for char in text:
        compressed_text += codes[char]

    return compressed_text, codes


# 使用哈夫曼编码解压缩文本
def decompress_text(compressed_text, codes):
    reversed_codes = {code: char for char, code in codes.items()}

    decompressed_text = ''
    code = ''
    for bit in compressed_text:
        code += bit
        if code in reversed_codes:
            char = reversed_codes[code]
            decompressed_text += char
            code = ''

    return decompressed_text


# 示例用法
text = "Hello, world!"
compressed_text, codes = compress_text(text)
print("Compressed Text:", compressed_text)
print("Huffman Codes:", codes)
decompressed_text = decompress_text(compressed_text, codes)
print("Decompressed Text:", decompressed_text)