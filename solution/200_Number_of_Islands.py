from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0: return 0
        
        row = len(grid)
        col = len(grid[0])
        island_num = 0
        
        direction = [(0,-1), (0,1), (-1,0), (1,0)] #Top, Down, Left, Right
        adjacent_queue = deque()
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    grid[r][c] == "#" #marked as visited
                    island_num += 1
                    
                    adjacent_queue.append((r,c)) 
                    while(len(adjacent_queue) > 0):
                        cur_r, cur_c = adjacent_queue.popleft()
                        for d in direction:
                            a_r, a_c = cur_r + d[0], cur_c + d[1]
    
                            if a_r >= 0 and a_r < row and a_c >= 0 and a_c < col and grid[a_r][a_c] == "1":
                                grid[a_r][a_c] = "#" #marked as visited
                                adjacent_queue.append((a_r,a_c)) #continue to check the adjacent to see how big the island is

        return island_num
        
