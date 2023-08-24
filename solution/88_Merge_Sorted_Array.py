class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i, j, write_index = m-1, n-1, m+n-1
        while j >=0:
            if i >=0 and nums1[i] > nums2[j]:
                nums1[write_index] = nums1[i]
                i-=1
            else:
                nums1[write_index] = nums2[j]
                j-=1
            write_index-=1

