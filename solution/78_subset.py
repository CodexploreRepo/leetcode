class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res, n = [[]], len(nums)

        def backtracking(cur_subset, remain_nums):
            m = len(remain_nums)
            if len(cur_subset) == n:
                return

            for i in range(m):
                temp = cur_subset[:]
                temp.append(remain_nums[i])
                res.append(temp)
                if i < m - 1:
                    backtracking(temp, remain_nums[(i + 1) :])

        if nums:
            backtracking([], nums)
        return res
