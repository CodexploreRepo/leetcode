class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        # initialise left and right pointer
        l, r = 0, 1
        sub_set, max_len = set(s[l]), 1

        # ensure that r pointer is not exceed then len(s)
        while r < len(s):
            if s[r] not in sub_set:
                sub_set.add(s[r])
                max_len = max(max_len, len(sub_set))
                r += 1
            else:
                # if r in the sub_set, we will remove the left-most item out of the sub_set
                # increase l pointer to the next pos
                sub_set.remove(s[l])
                l += 1

        return max_len
