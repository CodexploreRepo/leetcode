# Problem Set

# Arrays & Hashing

| Problems                                                                     | Difficulty | Tips                                                                                             |                   Solutions                    | Complexity                                                                                                             |
| :--------------------------------------------------------------------------- | :--------: | :----------------------------------------------------------------------------------------------- | :--------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------- |
| [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)  |   `Easy`   | **3 Pointers + Backward Move**                                                                   | [Code](.././solution/88_Merge_Sorted_Array.py) | Time $O(n)$<br> Space $O(1)$ in-place array modification                                                               |
| [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) |   `Easy`   | **Hash Set** <br> Alternative: Sort & then takes $O(n)$ to compare, but sorting costs $O(nlogn)$ |                                                | Time $O(n)$<br> Space $O(n)$                                                                                           |
| [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)           |   `Easy`   | **Hash Set**                                                                                     |                                                | Time $O(n)$<br> Space $O(n)$                                                                                           |
| [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)          |  `Medium`  | **Sorting + Hash Set**                                                                           |                                                | Time: $O(n * (a*log(a))$ <br>where a is max length of strings in the list, where n is the length of the list of string |

## Sliding Windows

| Problems                                                                                                                           | Difficulty |                                 Solutions                                 | Description                                                                                                   |
| ---------------------------------------------------------------------------------------------------------------------------------- | :--------: | :-----------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------ |
| [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)                             |   `Easy`   |       [Code](.././solution/121_Best_Time_to_Buy_and_Sell_Stock.py)        | Need to keep track on buy price with the next days                                                            |
| [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) |  `Medium`  | [Code](.././solution/3_Longest_Substring_Without_Repeating_Characters.py) | Need to have a start pointer along with i to loop through each element and a hash table to store the location |
| [438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)                                 |  `Medium`  |        [Code](../solution/438_Find_All%20Anagrams_in_a_String.py)         | Need to have hash_map to store the counts of `s` and `p`, and comparing the count                             |

## Linked List

| Problems                                                                                                   | Difficulty |                        Solutions                         | Description                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------- | :--------: | :------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)                             |   `Easy`   |     [Code](.././solution/206_Reverse_Linked_List.py)     |                                                                                                                                                                        |
| [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)                                 |   `Easy`   |      [Code](.././solution/141_Linked_List_Cycle.py)      | **Floyd's Tortoise and Hare Algorithm**: Use 2 pointers slow fast to traverse, if slow meets fast, meaning it is a cycle linked list                                   |
| [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)                        |   `Easy`   |    [Code](.././solution/21_Merge_Two_Sorted_List.py)     | Use 2 pointers to traverse the two lists                                                                                                                               |
| 160. Intersection of Two Linked Lists                                                                      |   `Easy`   |    [Code](.././solution/92_Reverse_Linked_List_II.py)    | Please refer the comment                                                                                                                                               |
| [203. Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/description/) |   `Easy`   | [Code](.././solution/203_Remove_Linked_List_Elements.py) | Create a dummy head and connect it the head, to prevent the case that we need to remove the head                                                                       |
| [143. Reorder List](https://leetcode.com/problems/reorder-list/)                                           |  `Medium`  |        [Code](.././solution/143_Reorder_List.py)         | **Step 1**: Find the middle point of the linked list <br>**Step 2**: Reverse the second half of the linked list<br>**Step 3**: Merge first & second half alternatively |

## Stack

| Problems              | Difficulty |                   Solutions                   | Description |
| --------------------- | :--------: | :-------------------------------------------: | :---------- |
| 20. Valid Parentheses |   `Easy`   | [Code](.././solution/20_Valid_Parentheses.py) | Using Stack |

## Tree

| Problems                                                                                                      | Difficulty |                         Solutions                         | Description     |
| ------------------------------------------------------------------------------------------------------------- | :--------: | :-------------------------------------------------------: | :-------------- |
| [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/description/) |   `Easy`   | [Code](.././solution/94_Binary_Tree_Inorder_Traversal.py) | Using Recursion |
| [100. Same Tree](https://leetcode.com/problems/same-tree/)                                                    |   `Easy`   |          [Code](.././solution/100_Same_Tree.py)           |                 |
| [101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/description/)                              |   `East`   |        [Code](.././solution/101_Symmetric_Tree.py)        |                 |
| [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/description/)                  |   `East`   |     [Code](.././solution/110_Balanced_Binary_Tree.py)     |                 |

## Binary Search (Tree)

- Hints: sorted arrays

| Problems                                                                               | Difficulty |                   Solutions                    | Description                                             |
| -------------------------------------------------------------------------------------- | :--------: | :--------------------------------------------: | :------------------------------------------------------ |
| [704. Binary Search](https://leetcode.com/problems/binary-search/description/)         |   `Easy`   |   [Code](.././solution/704_Binary_Search.py)   |                                                         |
| [278. First Bad Version](https://leetcode.com/problems/first-bad-version/description/) |   `Easy`   | [Code](.././solution/278_First_Bad_Version.py) | Using the binary search to narrow down the search space |

## BFS

### BFS Tree

| Problems                                                                                                               | Difficulty |                           Solutions                            | Description |
| ---------------------------------------------------------------------------------------------------------------------- | :--------: | :------------------------------------------------------------: | :---------- |
| [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/description/) |  `Medium`  | [Code](.././solution/102_Binary_Tree_Level_Order_Traversal.py) | Using BFS   |

### BFS Graph

| Problems                                                                   | Difficulty |                   Solutions                    | Description                                                                                                                                                                      |
| -------------------------------------------------------------------------- | :--------: | :--------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) |  `Medium`  | [Code](.././solution/200_Number_of_Islands.py) | Need to go through all the cells in the grid and then search adjacent location (top, down, left, right) of the "1" cell to find the maximum size of an island, then can continue |

## Dynamic Programming

| Problems                                                                                             | Difficulty |                       Solutions                       | Description                                                                                                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------- | :--------: | :---------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [509. Fibonacci Number](https://leetcode.com/problems/fibonacci-number/description/)                 |   `Easy`   |     [Code](.././solution/509_Fibonacci_Number.py)     |                                                                                                                                                                                                                                                      |
| 70. Climbing Stairs                                                                                  |   `Easy`   |      [Code](.././solution/70_Climbing_Stairs.py)      | At T(n): first step = 1, remaining steps = T(n-1) or first step = 2, remaing steps = T(n-2). This recurrence relationship is similar to Fibonacci number                                                                                             |
| [746. Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/description/) |   `Easy`   | [Code](.././solution/746_Min_Cost_Climbing_Stairs.py) | Recurrence relationship: `total_cost[i] = min(total_cost[i-1], total_cost[i-2]) + cost[i]` <br>Final Cost: `total_cost[n] = min(total_cost[n-1], total_cost[n-2])` as no need to include the `cost[n]`                                               |
| [64. Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/description/)                  |  `Medium`  |     [Code](.././solution/64_Minimum_Path_Sum.py)      | Recurrence relationship: `grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]                                 ` <br>Note: Need to update the first row `grid[0][j]` and first column `grid[i][0]` before can start the recurrence relationship |

## Backtracking

| Problems                                                                               | Difficulty | Tips          |                             Solutions                             | Complexity                                                                                                                                                                                      |
| :------------------------------------------------------------------------------------- | :--------: | :------------ | :---------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/target-sum/) |  `Medium`  | Back-tracking | [Code](.././solution/17_Letter_Combinations_of_a_Phone_Number.py) | Time: $O(n * 4^n)$ <br> Space: <br>where `n` = len of digits, and m is len of character set that corresponding to each digit, in this case max `m = 4`                                          |
| [Subset](https://leetcode.com/problems/subsets/description/)                           |  `Medium`  | Back-tracking |                [Code](.././solution/78_subset.py)                 | Time: $O(n * 2^n)$ where $2^n$ is total number of subsets and $n$ is to copy each subset to `res` <br> Space: $O(n)$ as we need a `temp` array and `curr_subset` <br>where `n` = length of nums |
| [494. Target Sum](https://leetcode.com/problems/target-sum/)                           |  `Medium`  | Back-tracking |                                                                   |                                                                                                                                                                                                 |
