class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_str, max_len, cur_str = "", 0, ""
        n = len(s)
        for i in range(n):
            #Check Odd Pal: cabac -> Need to check left (a) and right (a) of i (b) if they are equal
            cur_str, cur_len  = self.check_pal(s, n, i-1, i+1)
           
            if cur_len > max_len: max_str, max_len = cur_str, cur_len
            
            #Check Even Pal: abba -> Need to check left (b) and right (b) if they are equal
            cur_str, cur_len = self.check_pal(s, n, i, i+1)
            if cur_len > max_len: max_str, max_len = cur_str, cur_len

        return max_str
    
    def check_pal(self, s, n, j, k):
        while(j >= 0 and k < n):
            if s[j] != s[k]: break
            j-=1
            k+=1
        
        return s[j+1:k], len(s[j+1:k])
