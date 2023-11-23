class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n, m, result = len(s), len(p), []
        if n < m:
            return result
        count_s, count_p = {}, {}
        for c_i in range(m):
            count_p[p[c_i]] = 1 + count_p.get(p[c_i], 0)
            count_s[s[c_i]] = 1 + count_s.get(s[c_i], 0)

        if count_p == count_s:
            result.append(0)

        l = 0
        for r in range(m, n):
            # add the next char'scount into the count_s
            count_s[s[r]] = 1 + count_s.get(s[r], 0)
            # remove the char's count at left pointer
            count_s[s[l]] -= 1
            # if the char's count at left pointer is 0, pop out of the count_s
            if count_s[s[l]] == 0:
                count_s.pop(s[l])
            # move l to the cur pos that form the sub_str
            l += 1
            if count_p == count_s:
                result.append(l)
        return result
