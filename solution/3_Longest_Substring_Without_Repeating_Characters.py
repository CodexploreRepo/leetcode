class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        left, right, n = 0, 1, len(s)

        max_length, sub_str = 1, {s[left]: left}

        while right < n:
            if s[right] not in sub_str:
                sub_str[s[right]] = right
                max_length = max(max_length, len(sub_str))

            else:
                # move the left pointer to (first occurence) + 1 of the repeated char
                left = sub_str[s[right]] + 1
                # re-create the sub-string
                sub_str = {s[i]: i for i in range(left, right + 1)}

            right += 1
        return max_length
