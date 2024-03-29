# Daily Knowledge

## Day 2

### Top Coding Interview Concepts

- Hash Map: duplicate, count
- Recursion: Backtracking, DP
- DFS & BFS
- Binary Search
- Sliding Window
- Heap: Top K

## Day 1

### Backtracking

- [Back Tracking](./docs/algorithm/backtracking.md)
  - **Usage**: generate all combinations, permuations, subsets
  - **Brief Explain**: Backtracking can be seen as an optimized way to brute force which is to evaluate every possibility. In backtracking you stop evaluating a possibility as soon it breaks some constraint provided in the problem.

#### Combination

##### Subset

- How to determine the possible number of the subsets:
  - For each number in a set of length `n`, we have two choices: include or not include into the subset, so the total possible subsets is $2^n$
