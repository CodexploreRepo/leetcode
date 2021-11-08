class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")]*(amount+1)
        dp[0] = 0
        n = len(coins)
        
        for i in range(1, amount+1):
            for j in range(n):
                if coins[j] <= i:
                    dp[i] = min(dp[i], 1+ dp[i-coins[j]])
        return dp[-1] if dp[-1] != float("inf") else -1
        
