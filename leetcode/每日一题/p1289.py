grid = [[1,2,3],[4,5,6],[7,8,9]]

# grid[i][j] = min(grid[i-1]) + grid[i][j] except grid[i-1][j]
def min_falling_path_sum(grid):
    for i in range(1, len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] += min(grid[i-1][:j]+grid[i-1][j+1:])
    return min(grid[-1])
