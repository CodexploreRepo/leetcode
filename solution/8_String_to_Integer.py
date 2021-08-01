class Solution:
    def myAtoi(self, s: str) -> int:
        '''
        Valid
        '42' -> 42
        '   -42' -> -42
        '99999999999999' -> MAX_INT
        '1312zcxvzc' -> 1312
        
        Invalid
        'asdfas'  -> 0
        '  +asdkljfasd 9' -> 0
        '' -> 0
        
        1. whitespace
        2. a +/- symbol
        3. numbers
        4  between MAX_INT and MIN_INT constraints
        5. random characters
        
        Time O(n)
        Space O(1)
        
        n is the number of characters in your input string
        '''

        MAX_INT = 2 ** 31 - 1 # 2147483647
        MIN_INT = -2 ** 31    #-2147483648
        
        i = 0
        res = 0
        sL = len(s)
        sign = 1
        
        #Remove whitespace
        while (i < sL and s[i] == ' '):
            i+=1
        
        # +/- sign
        if i < sL and s[i] == '-':
            sign = -1
            i+=1
        elif i < sL and s[i] == '+':
            i+=1
        
        nums = set('0123456789')
        while (i < sL and s[i] in nums):
            if res > MAX_INT//10 or (res == MAX_INT//10 and int(s[i]) > 7):
                return MAX_INT if sign == 1 else MIN_INT
            res = res*10 + ord(s[i]) - ord('0')
            i+=1
        
        # res = res*sign
        # if res < 0:
        #     return max(res, MIN_INT)
        # else:
        #     return min(res, MAX_INT)
        
        return res*sign
  
        
            
