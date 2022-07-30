# Leetcode

# Arrays & Hashing

| Problems   | Difficulty |     Solutions      |  Complexity |
|----------  |:----------:|:------------------:|:-------------|
|[217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)|`Easy`| Hash Set| Time Complexity `O(n)`<br> Space Complexity `O(n)`|

## Hash Set
```Python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
```
