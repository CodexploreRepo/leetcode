class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        x^10 = x^5 * x^5. 
        Now we have odd power, but it is not a problem, 
        we evaluate x^5 = x^2 * x^2 * x. 
        
        Special Case: If we have n < 0 negative power, return positive power of 1/x.
        Base Case:
        If we have n = 0, return 1 as x^(0) = 1
        If we have n = 1, return 1 as x^(0) = x
        
        Recursive Case:
        Now, we have two cases: for even and for odd n, where we evaluate power n//2, i.e: M = myPow(x, n//2)
        Even: return M*M
        Odd: return M*x*M
        """
        #if n < 0, convert n > 0, convert x to 1/x
        if n < 0: return self.myPow(1/x, -n)
        #Base Case
        if n == 0: return 1
        if n == 1: return x
       
        M = self.myPow(x, n//2)
        if (n%2 == 0):
            return M*M
        else:
            return M*x*M
