class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s:
            a = [i for i in s.lower() if i.isalnum()] 
            return a == a[::-1]
        else:
            return True
            
