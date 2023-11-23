# Binary Search

## Introduction

- A binary search tree is a binary tree with the following property at all nodes:
  - Every key in the left subtree is smaller than itself
  - Every key in the right subtree is larger than itself
- In-order traversal of binary search trees are sorted lists
- Binary Search helps us reduce the search time from linear $O(n)$ to logarithmic $O(log(n))$.

```Python
def binary_search(array) -> int:

    left, right = min(search_space), max(search_space) # could be [0, n], [1, n] etc. Depends on problem
    while left < right:
        mid = left + (right - left) // 2 # determine the mid point
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left
```

## Resources

- [Ultimate Binary Search Template](https://leetcode.com/discuss/study-guide/786126/Python-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems)
