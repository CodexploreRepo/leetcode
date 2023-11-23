class Solution(object):
    """
    Bottom-Up Solution
    """

    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        n = len(cost)
        dp = [0] * n
        dp[0], dp[1] = cost[0], cost[1]
        # recurrence relationship:
        # total_cost[i] = min(total_cost[i-1], total_cost[i-2]) + cost[i]
        # total_cost[n] = min(total_cost[n-1], total_cost[n-2]) as no need to include the cost[n]
        for i in range(2, n):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        return min(dp[n - 1], dp[n - 2])
