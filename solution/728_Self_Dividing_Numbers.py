class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
     
        for num in range(left, right + 1):
            divisible = True
            n = num
            
            while n > 0:
                d = n%10
                if (d == 0) or (num % d != 0):
                    divisible = False
                    break
                n //=10
                
            if divisible:
                result.append(num)
        return result
                
