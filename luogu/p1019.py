n = int(input())
words = []
for _ in range(n):
    word = input()
    words.append(word)
    # words.append(word)
ch = input()

maxl = 0
# def backtrack(s,word):
#     if word.starswith(s)
res = []

for word in words:
    if word.starswith(ch):
        