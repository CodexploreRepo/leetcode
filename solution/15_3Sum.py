class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort() #Sort the array in ascending order
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue #fi nums[i] = previous (i-1), we will skip as the soln for nums[i] and for nums[i-1] will be duplicated
            j = i + 1
            k = n - 1
            while(j < k):
                cur_sum = nums[i] + nums[j] + nums[k]
                if cur_sum == 0:
                    #i, j, k = 0 
                    res.append([nums[i], nums[j], nums[k]])
                    #so if j < k, we might need to increase j and decrease k to find another combination of fixed i and new j, k
                    while j < k and nums[j] == nums[j+1]: #to ensure that nums[j+1] != nums[j], otherwise the soln will be duplicated
                        j += 1
                    while j < k and nums[k] == nums[k-1]: #to ensure that nums[k-1] != nums[k], otherwise the soln will be duplicated
                        k -= 1
                    j += 1; k -= 1 #increase j and decrease k to find another combination of fixed i and new j,k
                if cur_sum < 0: j+=1 #if sum < 0, need to increase j as the values in array is sorted in ascending order
                if cur_sum > 0: k-=1 #if sum > 0, need to decrease k as the values in array is sorted in ascending order 
        
        return res
