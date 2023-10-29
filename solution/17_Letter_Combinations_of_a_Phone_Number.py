class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letters = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        res = []
        n = len(digits)

        def backtracking(index, curr_str):
            # Base Case:
            if len(curr_str) == n:
                res.append(curr_str)
                return
            # Recursive Case:
            for letter in letters[digits[index]]:
                backtracking(index + 1, curr_str + letter)

        if digits:
            # ensure that there is no empty
            backtracking(0, "")
        return res
