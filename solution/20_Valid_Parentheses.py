class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 1:
            return False

        stack_ds = []
        pairs = {
            "(": ")",
            "{": "}",
            "[": "]",
        }
        for c in s:
            if c in pairs:
                stack_ds.append(c)
            else:
                if stack_ds == [] or pairs[stack_ds.pop()] != c:
                    return False
        else:
            return stack_ds == []
