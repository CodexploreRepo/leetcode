class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        dp = [[0]*(n2+1) for _ in range(n1+1)]
        for i in range(n2+1):
            dp[n1][i] = n2-i
        for j in range(n1+1):
            dp[j][n2] = n1-j
        for i in range(n1-1, -1, -1):
            for j in range(n2-1,-1,-1):
                dp[i][j] = min(dp[i][j+1] + 1, dp[i+1][j] + 1, dp[i+1][j+1] + (word1[i] != word2[j]))
        return dp[0][0]
