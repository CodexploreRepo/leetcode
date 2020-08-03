#Math: 1 + 2 + 3 + 4 + .. k levels = [k(k+1)]/2 ≤ n => Find k will be the level of stair cases
 
class Solution:
    def arrangeCoins(self, n: int) -> int:
         return (int)((2 * n + 0.25)**0.5 - 0.5)
