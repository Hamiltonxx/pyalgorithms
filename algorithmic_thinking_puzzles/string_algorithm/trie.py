def make_trie(words):
    trie = {}
    for word in words:
        h = trie 
        for c in word:
            h = h.setdefault(c,{})
        h['$'] = '$'
    return trie 

def in_trie(trie, word):
    h = trie
    for c in word:
        if c not in h:
            return False
        h = h[c]
    return '$' in h  

def insert_trie(trie, word):
    h = trie
    for c in word:
        h = h.setdefault(c, {})
    h['$'] = '$'
    return trie

