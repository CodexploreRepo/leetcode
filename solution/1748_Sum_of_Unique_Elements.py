class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)

        return sum([key for key, value in counts.items() if value == 1])
