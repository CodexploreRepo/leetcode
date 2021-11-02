class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n, max_sum = len(nums), float("-inf")
        dp = [float("-inf")]*(n+1)
        for i in range(1, n+1):
            dp[i] = max(nums[i-1],nums[i-1] + dp[i-1])
            max_sum = max(dp[i], max_sum)
        return max_sum
