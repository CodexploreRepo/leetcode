class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first, second = 0, 0 
        #Find the 2 maximum element in the 
        for number in nums:
            if number > first:
                second = first
                first = number
            elif second < number:
                second = number
        return (first -1)*(second -1)
            
