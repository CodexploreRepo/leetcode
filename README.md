# Leetcode

# Arrays & Hashing

| Problems   | Difficulty |     Solutions      |  Complexity |
|----------  |:----------:|:-------------------|:-------------|
|[217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)|`Easy`| **Hash Set** <br> Alternative: Sort & then takes `O(n)` to compare, but sorting costs `O(nlogn)` | Time Complexity `O(n)`<br> Space Complexity `O(n)`|
|[242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)|`Easy`| **Hash Set** |Time Complexity `O(n)`<br> Space Complexity `O(n)`|

## Hashing
- Hashing can be implemented via `set` or `dict`
### Hash Set
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
### Hash Map
```Python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        from collections import defaultdict
        hash_map = defaultdict(lambda: 0) #using defaultdict
        for elem in nums:
            hash_map[elem] += 1
            if hash_map[elem] > 1:
                return True
            
        else:
            return False
```
