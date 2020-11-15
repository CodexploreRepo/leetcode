<!-- Add banner here -->

# LeetCode Solution
This is powered by CodeXplore 

# Table of contents

<!-- After you have introduced your project, it is a good idea to add a **Table of contents** or **TOC** as **cool** people say it. This would make it easier for people to navigate through your README and find exactly what they are looking for.

Here is a sample TOC(*wow! such cool!*) that is actually the TOC for this README. -->

- [Table of contents](#table-of-contents)
- [Tips and Tricks](#tips-and-tricks)
- [Data Structure](#data-structure)
- [Algorithms](#algorithms)
    - [Searching](#searching)
- [LeetCode Solutions](#leetcode-solutions)
    - [String](#string)
    - [Binary Tree - BFS & DFS](#binary-tree)
    - [Others](#others)
- [Resources](#resources)
- [License](#license)

# Tips and Tricks
### Binary Number
- [Convert Binary Number to Integer](/1290_convert_Binary_to_Integer.js) For ex: LinkedList of Binary: 1 -> 0 -> 1 = 5 in decimal
    - Tips: Bitwise operation 
        -  initialise an integer variable num to 0
        - `num << 1` left shift `num` by 1 position to make way for the val in the next node in linked list. This is same as multiplying num by 2
        - `num << 1 | head.val` Add (|) next bit to num at least significant position
    


# Data Structure
# Algorithms

### Searching
| Algo Name   |      Note      | 
|----------|:-------------:|
|[Breadth First Search (BFS)](/algorithm/searching/breadthFirstSearch.js)| Shortest Path; Closer Nodes|


# LeetCode Solutions
### String

| Problems   |      Solutions      |  Description |
|----------|:-------------:|:------|
|[125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)|[Code](/125_Valid_Palindrome.py)| Check if original & reverse string are the same (ie: return *result == result[ : : -1])*|
| [344. Reverse String](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)|[Code](/344_Reverse_String.py) | 2-pointer approach to reverse the string without creating extra memory (i.e: Space Complexity O(1)|

### Binary Tree

| Problems   |      Solutions      |  Description |
|----------|:-------------:|:------|
| [107. Binary Tree Level Order Traversal II](https://leetcode.com/problems/reverse-string/)|[Code](/107_Binary_Tree_Level_Order_Traversal_II.py) | BFS + Each Tree Level Traversal <br> <img src="https://user-images.githubusercontent.com/64508435/89198914-71fcb980-d5e0-11ea-9f4b-77ae4364bd1b.JPG" width="500" />|

[(Back to top)](#table-of-contents)
### Others

| Problems   |      Solutions      |  Tips |
|----------|:-------------:|:------|
| [441. Arranging Coins](https://leetcode.com/problems/arranging-coins/)|  [Code](/441_Arranging_Coins.py) | Using Mathematics Formula |
| [1290. Convert Binary Number in a Linked List to Integer](https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/)|  [Code](/1290_convert_Binary_to_Integer.js) | Use Bit Shift |

# Resources
[Data Structure & Algo - TypeScript](https://github.com/CoffeelessProgrammer/Data-Structures-and-Algorithms-TS)


[(Back to top)](#table-of-contents)

# License
© Copyright by CodeXplore ☞ Do not Reup <br>
[(Back to top)](#table-of-contents)


