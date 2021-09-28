class Solution:
    memo = {1: 1, 2:2} #T(1) = 1, i.e: only 1 way to climb up the stair = 1, and T(2) = 2 as 2 ways to climb up the stair = 2
    def climbStairs(self, n: int) -> int:
        if n not in self.memo: 
            #@ T(n): first step = 1, remaining steps = T(n-1) or first step = 2, remaing steps = T(n-2)
            self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2) 
        return self.memo[n]
