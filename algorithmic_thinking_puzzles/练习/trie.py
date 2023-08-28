def make_trie(words):
    trie = {}
    for word in words:
        head = trie 
        for char in word:
            head = head.setdefault(char,{})
        head["_end"] = "_end"
    return trie 