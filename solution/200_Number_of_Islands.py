class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        row, col = len(grid), len(grid[0])
        num_islands = 0

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    # need to marked the cell as visited as below BFS might add this pos again
                    grid[r][c] = "#"
                    num_islands += 1
                    queue = [(r, c)]

                    while len(queue) > 0:
                        cur_r, cur_c = queue.pop(0)

                        for d_r, d_c in directions:
                            next_r, next_c = cur_r + d_r, cur_c + d_c
                            if (next_r >= 0 and next_r < row) and (
                                next_c >= 0 and next_c < col
                            ):
                                if grid[next_r][next_c] == "1":
                                    # marked the next cell as visited
                                    grid[next_r][next_c] = "#"
                                    queue.append((next_r, next_c))

        return num_islands
