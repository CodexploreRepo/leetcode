class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*(n)
        dp[n-1] = nums[n-1]
        dp[n-2] = nums[n-2]
        for i in range(n-3, -1, -1):
            for j in range(i, n-2):
                dp[i] = max(dp[i], nums[i] + dp[j+2])
        return max(dp)
