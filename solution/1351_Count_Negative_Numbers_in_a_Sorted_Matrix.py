# Solution 1: Brute Force O(n^2)
class Solution1:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        for i in range(0, rows):
            for j in range(0, cols):
                if grid[i][j] < 0:
                    count+=1
        return count
# Solution 2: 2 pointer approach - "trace" the outline of the staircase
# O(m + n)
class Solution2:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        r, c, result = m-1, 0, 0
        while r >= 0 and c < n:
            if grid[r][c] < 0:
                result += n-c
                r-=1
            else:
                c+=1
                
        return result
# Solution 3: Binary Search - since Sorted Array
# m * log(n)
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def binarySearch(row):
            start = 0
            end = len(row) - 1
            
            while (start <= end):
                mid = start + (end - start)//2
                if (row[mid] < 0):
                    end = mid - 1
                else:
                    start = mid + 1
            
            return len(row) - start
        
        result = 0
        for row in grid:
            result += binarySearch(row)
        return result 
            
