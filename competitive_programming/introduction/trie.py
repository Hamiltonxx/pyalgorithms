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
    return '_end' in head

t = make_trie(["barz","bar"])
print(t)
print(in_trie(t, "barz"))