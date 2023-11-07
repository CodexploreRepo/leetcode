class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        m, n = len(grid), len(grid[0])
        # recurrence relationship:  grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        # update along the first row
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]
        # update along the first col
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
        # update cells apart from first row & first col
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]

        return grid[-1][-1]
