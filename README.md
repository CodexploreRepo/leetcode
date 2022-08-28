# Leetcode

# Arrays & Hashing

| Problems   | Difficulty |     Solutions      |  Complexity |
|----------  |:----------:|:-------------------|:-------------|
|[217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)|`Easy`| **Hash Set** <br> Alternative: Sort & then takes `O(n)` to compare, but sorting costs `O(nlogn)` | Time `O(n)`<br> Space `O(n)`|
|[242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)|`Easy`| **Hash Set** |Time `O(n)`<br> Space `O(n)`|
|[49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)|`Medium`|**Sorting + Hash Set** ||

# Python Tips
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
## Sorting
- `sorted(iterable, key=key, reverse=reverse)`
    - return a sorted list of the specified iterable object.
    
```Python
a = "azy"
x = sorted(a) #['a', 'y', 'z']
```
