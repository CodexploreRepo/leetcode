# Backtracking

## What is Backtracking ?

- Backtracking is a general algorithm for finding all (or some) solutions, that incrementally builds candidates to the solutions.
- Backtracking can be seen as an optimized way to brute force which is to evaluate every possibility. In backtracking you stop evaluating a possibility as soon it breaks some constraint provided in the problem.

### Properties and Applications

- Backtracking is like a depth-first search (DFS) with an added constraint that we stop exploring the subtree as soon as we know for sure that it won’t lead to valid solution.
- The problems that can be solved using this tool generally satisfy the following criteria :
  - You are explicitly asked to return **a collection of all answers**.
  - You are concerned with what the actual solutions are rather than say the most optimum value of some parameter. (if it were the latter it’s most likely DP or greedy).

### Procedure

- Step 1: Drawing the flow of the recursive function

### Example

#### [Subset](https://leetcode.com/problems/subsets/description/)

- The problem is to find the powerset of a given set, so we simply need to collect all possible subsets of a set.
- How to determine the possible number of the subsets:
  - For each number in a set of length `n`, we have two choices: include or not include into the subset, so the total possible subsets is $2^n$
- Ideas:
  - Branch 1: If we include the first item in the subset, say `[1]`, so the renaming choice to generate another the subset on top of `[1]` is either `[2,3]`
  - Branch 2: If we include the second in the subset, say `[2]`, so the renaming choice to generate another the subset on top of `[2]` is only `[3]` as we already has the subset `[1,2]` in the first branch
  <p align="center"><img src="../assets/img/78_subset.jpg"></p>
