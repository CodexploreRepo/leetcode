# Problem Set

# Arrays & Hashing

| Problems                                                                     | Difficulty | Tips                                                                                             |                   Solutions                    | Complexity                                                                                                             |
| :--------------------------------------------------------------------------- | :--------: | :----------------------------------------------------------------------------------------------- | :--------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------- |
| [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)  |   `Easy`   | **3 Pointers + Backward Move**                                                                   | [Code](.././solution/88_Merge_Sorted_Array.py) | Time $O(n)$<br> Space $O(1)$ in-place array modification                                                               |
| [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) |   `Easy`   | **Hash Set** <br> Alternative: Sort & then takes $O(n)$ to compare, but sorting costs $O(nlogn)$ |                                                | Time $O(n)$<br> Space $O(n)$                                                                                           |
| [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)           |   `Easy`   | **Hash Set**                                                                                     |                                                | Time $O(n)$<br> Space $O(n)$                                                                                           |
| [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)          |  `Medium`  | **Sorting + Hash Set**                                                                           |                                                | Time: $O(n * (a*log(a))$ <br>where a is max length of strings in the list, where n is the length of the list of string |

## Sliding Windows

| Problems                                                                                               | Difficulty |                                 Solutions                                 | Description                                                                                                   |
| ------------------------------------------------------------------------------------------------------ | :--------: | :-----------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------ |
| [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) |   `Easy`   |       [Code](.././solution/121_Best_Time_to_Buy_and_Sell_Stock.py)        | Need to keep track on buy price with the next days                                                            |
| 3. Longest Substring Without Repeating Characters                                                      |  `Medium`  | [Code](.././solution/3_Longest_Substring_Without_Repeating_Characters.py) | Need to have a start pointer along with i to loop through each element and a hash table to store the location |

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

| Problems                                                                                                               | Difficulty |                           Solutions                            | Description     |
| ---------------------------------------------------------------------------------------------------------------------- | :--------: | :------------------------------------------------------------: | :-------------- |
| [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/description/)          |   `Easy`   |   [Code](.././solution/94_Binary_Tree_Inorder_Traversal.py)    | Using Recursion |
| [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/description/) |  `Medium`  | [Code](.././solution/102_Binary_Tree_Level_Order_Traversal.py) | Using BFS       |
| [100. Same Tree](https://leetcode.com/problems/same-tree/)                                                             |   `Easy`   |             [Code](.././solution/100_Same_Tree.py)             |                 |
| [101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/description/)                                       |   `East`   |          [Code](.././solution/101_Symmetric_Tree.py)           |                 |
| [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/description/)                           |   `East`   |       [Code](.././solution/110_Balanced_Binary_Tree.py)        |                 |

## Binary Search (Tree)

| Problems                                                                               | Difficulty |                   Solutions                    | Description                                             |
| -------------------------------------------------------------------------------------- | :--------: | :--------------------------------------------: | :------------------------------------------------------ |
| [704. Binary Search](https://leetcode.com/problems/binary-search/description/)         |   `Easy`   |   [Code](.././solution/704_Binary_Search.py)   |                                                         |
| [278. First Bad Version](https://leetcode.com/problems/first-bad-version/description/) |   `Easy`   | [Code](.././solution/278_First_Bad_Version.py) | Using the binary search to narrow down the search space |

## BFS

| Problems               | Difficulty |                   Solutions                    | Description |
| ---------------------- | :--------: | :--------------------------------------------: | :---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 200. Number of Islands | **Graph**  | [Code](.././solution/200_Number_of_Islands.py) | `Medium`    | Need to go through all the cells in the grid and then search adjacent location (top, down, left, right) of the "1" cell to find the maximum size of an island, then can continue |

## Dynamic Programming

| Problems                                                                               | Difficulty | Tips          |                           Solutions                            | Complexity                                                                                                                                                                                      |
| :------------------------------------------------------------------------------------- | :--------: | :------------ | :------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/target-sum/) |  `Medium`  | Back-tracking | [Code](./solution/17_Letter_Combinations_of_a_Phone_Number.py) | Time: $O(n * 4^n)$ <br> Space: <br>where `n` = len of digits, and m is len of character set that corresponding to each digit, in this case max `m = 4`                                          |
| [Subset](https://leetcode.com/problems/subsets/description/)                           |  `Medium`  | Back-tracking |                [Code](./solution/78_subset.py)                 | Time: $O(n * 2^n)$ where $2^n$ is total number of subsets and $n$ is to copy each subset to `res` <br> Space: $O(n)$ as we need a `temp` array and `curr_subset` <br>where `n` = length of nums |
| [494. Target Sum](https://leetcode.com/problems/target-sum/)                           |  `Medium`  | Back-tracking |                                                                |                                                                                                                                                                                                 |
