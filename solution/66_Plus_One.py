class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        leading = 0
        arrLen = len(digits)
        digits[-1]+=1
        for i in range(arrLen-1, -1, -1):
            digits[i]+=leading
            if digits[i]//10==1:
                digits[i]=0
                leading=1
                if i == 0:
                    digits.insert(0,1)
            else:
                leading = 0
        return digits
            
        
