class Solution:
    def sortString(self, s: str) -> str:
        dict, ans, desc = collections.Counter(s), [], False
       
        while len(ans) < len(s):
            for k in sorted(dict, reverse = desc):
                if dict[k] > 0:
                    ans.append(k)
                    dict[k] -= 1
                elif dict[k] == 0:
                    del dict[k]
            desc = ~desc
        return "".join(ans)
