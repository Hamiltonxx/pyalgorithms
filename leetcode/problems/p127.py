from collections import defaultdict, deque
def ladderLength(beginWord, endWord, wordList):
    L = len(beginWord)
    combo_dict = defaultdict(list)
    for word in wordList:
        for i in range(L):
            combo_dict[word[:i]+'*'+word[i+1:]].append(word)
    q = deque([(beginWord,1)])
    visited = {beginWord}
    while q:
        curword, level = q.popleft()
        for i in range(L):
            interword = curword[:i]+'*'+curword[i+1:]
            for word in combo_dict[interword]:
                if word == endWord:
                    return level + 1
                if word not in visited:
                    visited.add(word)
                    q.append((word, level+1))
    return 0