class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d_dict = {"2" : {"a", "b", "c"},
               "3" : {"d", "e", "f"},
               "4" : {"g", "h", "i"},
               "5" : {"j", "k", "l"},
               "6" : {"m", "n", "o"},
               "7" : {"p", "q", "r", "s"},
               "8" : {"t", "u", "v"},
               "9" : {"w", "x", "y", "z"}}
        res, n = [], len(digits)
        if n == 0: return ""
        digit = digits[0]
        if n == 1: return d_dict[digit]
        
        for char in d_dict[digit]:
            remain = self.letterCombinations(digits[1:])
            for s in remain:
                res.append(char+s)
        return res
