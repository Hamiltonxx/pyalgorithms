def rabin_karp_string_match(pattern, text):
    pl = len(pattern)
    tl = len(text)
    hsh = hash(pattern)
    for i in range(tl-pl+1):
        if hash(text[i:i+pl]) == hsh:
            if text[i:i+pl] == pattern:
                return i 
    return -1
# hash()计算复杂度与字符串长度成正比，对于较长字符串可能会很耗时
# 计算下一个hash值时，要用滚动hash(自定义hash)
text,pattern = "hello","el"
print(rabin_karp_string_match(pattern, text))

def rabin_karp_str_match(text, pattern):
    tl = len(text)
    pl = len(pattern)
    phash = sum([ord(x) for x in pattern])
    thash = sum([ord(text[i]) for i in range(pl)])
    if phash==thash:
        return 0 if text.startswith(pattern) else -1
    for i in range(1,tl-pl+1):
        thash -= ord(text[i-1])
        thash += ord(text[i+pl-1])
        if thash == phash:
            if text[i:i+pl] == pattern:
                return i
    return -1

text,pattern = "3141592653589793", "26"
print(rabin_karp_str_match(text,pattern))

