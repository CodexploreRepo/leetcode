class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Array - Hashing: Set -> O(n)
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            else:
                num_set.add(num)
        else:
            return False

        
