class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        2 0 2 1 1 0
        
        
        0 2 2 1 1 0
        0 0 2 1 1 2
        0 0 1 1 2 2 = results
        
        Dutch National Flag Problem
        Time: O(n)
        Space: O(1)
        """
        pivot = 1
        
        #First Sort: Move elements (0) smaller than pivot = (1) to LEFT
        smaller = 0 
        for i in range(0, len(nums)):
            if nums[i] < pivot:
                nums[smaller], nums[i] = nums[i], nums[smaller]
                smaller+=1
       
        #Second Sort: Move elements (2) larger than pivot = (1) to RIGHT
        larger = len(nums)-1
        for i in reversed(range(0, len(nums))):
            if nums[i] > pivot:
                nums[larger], nums[i] = nums[i], nums[larger]
                larger-=1
            elif nums[i] < pivot:
                break
            
            
            
