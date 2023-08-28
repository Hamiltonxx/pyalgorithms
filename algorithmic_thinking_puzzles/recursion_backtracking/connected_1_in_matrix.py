# Find the length of connected cells of 1s(regions) in a matrix of 0s and 1s
# 1 1 0 0 0
# 0 1 1 0 0
# 0 0 1 0 1
# 1 0 0 0 1
# 0 1 0 1 1

def get_region_lengths(matrix):
    row_len = len(matrix)
    col_len = len(matrix[0])
    visited = set()
    region_lengths = []

    def dfs(row, col, length):
        if row<0 or row>=row_len or col<0 or col>=col_len or (row,col) in visited or matrix[row][col]==0:
            return length 
        visited.add((row,col))
        length += 1
        length = dfs(row-1, col, length)
        length = dfs(row+1, col, length)
        length = dfs(row, col-1, length)
        length = dfs(row, col+1, length)
        return length
    
    for row in range(row_len):
        for col in range(col_len):
            if matrix[row][col]==1 and (row,col) not in visited:
                region_lengths.append(dfs(row,col,0))
    
    return region_lengths

matrix = [[1,1,0,0,0],[0,1,1,0,0],[0,0,1,0,1],[1,0,0,0,1],[0,1,0,1,1]]
print(get_region_lengths(matrix))
print(max(get_region_lengths(matrix)))