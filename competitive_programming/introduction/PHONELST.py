def make_trie(words):
    trie = {}
    for word in words:
        head = trie 
        for char in word:
            head = head.setdefault(char, {})
        head['_end'] = '_end'
    return trie

def check_cover(trie, word):
    head = trie 
    for char in word:
        head = head[char]
    return len(head) != 1

from sys import stdin 
t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    words = [stdin.readline().strip() for _ in range(n)]
    trie = make_trie(words)
    for word in words:
        if check_cover(trie,word):
            print("NO")
            break
    else:
        print("YES")

# words = ["113","12340","12344"]
# words = ["911","97625999","91125426"]
# trie = make_trie(words)
# for word in words:
#     if check_cover(trie, word):
#         print("NO")
#         break
# else:
#     print("YES")
