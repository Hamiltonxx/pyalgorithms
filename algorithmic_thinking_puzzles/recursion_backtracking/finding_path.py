# 1 1 0 0
# 0 1 1 0
# 0 0 1 0
# 0 0 1 1
# 回溯算法的时间复杂度很高(O(k^3)),通常使用BFS来解决路径搜索问题

from collections import deque 

def bfs_path_finding(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    # 定义起点和终点
    start_row, start_col = start 
    end_row, end_col = end 
    # 定义四个方向
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    # 初始化队列，将起点加入队列
    queue = deque([(start_row, start_col, 0)])
    visited = [[False] * cols for _ in range(rows)]
    visited[start_row][start_col] = True 
    
    while queue:
        row, col, distance = queue.popleft()
        # 如果当前位置为终点，返回距离
        if row==end_row and col==end_col:
            return distance 
        # 否则，遍历四个方向
        for d in directions:
            next_row, next_col = row+d[0], col+d[1]
            # 如果下一个位置在迷宫内部，且没有访问过，且不是障碍物，则加入队列
            if 0<=next_row<rows and 0<=next_col<cols and not visited[next_row][next_col] and maze[next_row][next_col]!=0:
                queue.append((next_row,next_col,distance+1))
                visited[next_row][next_col]=True
    # 如果无法到达终点，返回-1
    return -1

maze = [[1,1,0,0],[0,1,1,0],[0,0,1,0],[0,0,1,1]]
print(bfs_path_finding(maze,(0,0),(3,3))) 


# 改成返回路径
def finding_path_bfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    start_row, start_col = start 
    end_row, end_col = end 
    
    queue = deque([(start_row,start_col,[(start_row,start_col)])])
    visited = [[False]*cols for _ in range(rows)]
    visited[start_row][start_col] = True 
    directions = [(1,0),(-1,0),(0,1),(0,-1)]

    while queue:
        row, col, path = queue.popleft()
        if row==end_row and col==end_col:
            return path
        for d in directions:
            next_row, next_col = row+d[0], col+d[1]
            if 0<=next_row<rows and 0<=next_col<cols and not visited[next_row][next_col] and maze[next_row][next_col]!=0:
                newpath = path + [(next_row,next_col)]
                queue.append((next_row,next_col,newpath))
                visited[next_row][next_col] = True 
    
    return -1

print(finding_path_bfs(maze,(0,0),(3,3)))