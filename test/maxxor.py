def find_max_xor_sum(nums):
    max_xor_sum = 0
    xor_prefix = 0
    trie = {}

    for num in nums:
        # 更新前缀异或值
        xor_prefix ^= num

        # 插入前缀异或值到字典树
        node = trie
        for i in range(31, -1, -1):
            bit = (xor_prefix >> i) & 1
            if bit not in node:
                node[bit] = {}
            node = node[bit]

        # 计算当前前缀异或值与字典树中的最大异或值
        node = trie
        curr_xor_sum = 0
        for i in range(31, -1, -1):
            bit = (xor_prefix >> i) & 1
            if 1 - bit in node:
                node = node[1 - bit]
                curr_xor_sum |= (1 << i)
            else:
                node = node[bit]
        max_xor_sum = max(max_xor_sum, curr_xor_sum)

    return max_xor_sum

# 示例用法：
# nums = [3, 10, 5, 25, 2, 8]
# nums = [1,2,3,4]
# nums = [8, 1, 2, 12, 7, 6]
nums = [4, 6]
max_xor_sum = find_max_xor_sum(nums)
print(max_xor_sum)