# board = [["A","B","C","E"],
#          ["S","F","C","S"],
#          ["A","D","E","E"]]
# word = "ABCCED"
# word = "ABCB"
board = [["C","A","A"],
         ["A","A","A"],
         ["B","C","D"]]
word = "AAB"

def exist(board,word):
    m,n = len(board),len(board[0])
    def dfs(i,j,word):
        if not word:
            return True
        if i<0 or i>=m or j<0 or j>=n or board[i][j]!=word[0]:
            return False
        tmp = board[i][j]
        board[i][j]="#"
        res = dfs(i-1,j,word[1:]) or dfs(i+1,j,word[1:]) or dfs(i,j-1,word[1:]) or dfs(i,j+1,word[1:])
        board[i][j]=tmp
        return res
    for i in range(m):
        for j in range(n):
            if dfs(i,j,word):
                return True
    return False

print(exist(board,word))
