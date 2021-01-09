'''
Create arr_set: set of all numbers
Iterate i from 1 to k + len(arr): it will be enough to cover.
If we see missing number, we decrease k by 1.
Finally, if we see that k == 0, then we return i.
'''

class Solution:
    def findKthPositive(self, arr, k):
        arr_set = set(arr)
        for i in range(1, k + len(arr) + 1):
            if i not in arr_set: k -= 1
            if k == 0: return i
