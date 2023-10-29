# Python Tips

## List

- Copy a list: `copied_list = a_list[:]`
  - Leverage on `copy` module
  ```Python
  import copy
  copied_list = copy.deepcopy(a_list)
  ```

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
from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
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

### Sorting a Dict

- Based on values: `dict(sorted(name_diff.items(), key=lambda x: x[1], reverse = True))`
