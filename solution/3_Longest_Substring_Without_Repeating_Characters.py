class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_dict, max_sum, start = {}, 0, 0
        n = len(s)
        for i in range(n):
            if s[i] in char_dict and start <= char_dict[s[i]]:
                #start <= char_dict[s[i]]: To ensure that it will revert back to origin case
                start = char_dict[s[i]] + 1
            else:
                max_sum = max(max_sum, i - start + 1)
            char_dict[s[i]] = i
        return max_sum
