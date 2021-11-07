class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1,n+1):
                if i == 1 or j == 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
            
