class Solution:
    def isValid(self, s: str) -> bool:
        dict_lookup = {"(": ")", "{":"}", "[": "]"}
        stack = []

        for c in s:
            if c in dict_lookup.keys():
                stack.append(c)
            if c in dict_lookup.values():
                if stack == [] or c != dict_lookup[stack.pop()]:
                    return False 
        
        return stack == []
