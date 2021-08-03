<!-- Add banner here -->

# LeetCode Solution
This is powered by CodeXplore 

# Table of contents
- [Table of contents](#table-of-contents)
- [Part A: Data Structure](#part-a-data-structure)
- [1. Primitive Types](#1-primitive-types)
  - [1.1. KeyNotes](#11-keynotes)
  - [1.2. Bitwise Operation](#12-bitwise-operation)
  - [1.3. Strings and Numbers](#13-strings-and-numbers)
- [2. Arrays](#2-arrays)
  - [2.1. Keynotes](#21-keynotes)
  - [2.2. Array Problems](#22-array-problems)
- [3. Linked List](#3-linked-list)
  - [3.1. Keynotes](#31-keynotes) 
  - [3.2. Linked List Problems](#32-linked-list-problems)
- [Part B: Algorithms](#part-b-algorithms)
    - [Searching](#searching)
- [LeetCode Solutions](#leetcode-solutions)
    - [2D Matrix](#2d-matrix)
    - [Linked List](#linked-list)
    - [Binary Tree - BFS & DFS](#binary-tree)
    - [N-ary Tree - BFS & DFS](#n-ary-tree)
    - [Class Design](#class-design)
    - [Others](#others)
- [Resources](#resources)
- [License](#license)

# Part A: Data Structure
# 1. Primitive Types
## 1.1. KeyNotes
- [Number] Infinity: `float('inf')` and `float('-inf')`
- [Number] Math Operator: `%10` modulus 10 to extract last digit in a number, `//10` to remove the last digit in a number
- [Number > String] 9 to "9": `char(ord('0') + 9)`
- [String > Number] "9" to 9: `ord('9') - ord('0') = 9`, for s="123" to 123: `res = res*10 + ord(s[i]) - ord('0')`
- [String] Palindromic `all(s[i] == s[~i] for i in range(len(s//2))` where `s[~i] = s[-(i+1)]`
- [Set] Create a set of digits `['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']` => `nums = set('0123456789')`
## 1.2. Bitwise Operation:
- `x << y`: x is *Left* shifted by `2**y` same as multiplying x by `2**y` (and new bits on the right-hand-side are zeros).
- `x >> y`: x is *Right* shifted by `2**y` same as dividing x by `2**y` (and new bits on the left-hand-side are zeros).
- `x & 1` : compares LSB of X with 1 (For ex: x=1010, then `x & 0001` = 0)
- `x | 1` : add the LSB of X with 1  (For ex: x=1010, then `x | 0001` = 1011)
- :star: `x ^ 1` : XOR (`0 0 -> 0, 0 1 -> 1, 1 0 -> 1, 1 1 -> 0`)
- :star: `x&(x-1)`: to erase lowest set bit of x. (For ex: x=00101100, x-1= 00101011 then `x&(x-1)`=00101000)
### 1.2.1. Bitwise Example
- Question #1: Write a program to count number of bits set to 1 in a positive integer, say x = 69
```Python
num_bits = 0
while x:
    num_bits += x & 1 #Compare LSB of X with 1, if LSB = 1, then increase num_bits by 1
    x >>= 1 #Shift Right x by 1 bit
```
- Question #2: Computing Parity of Binary Word (parity = 1 when # of 1s in the word is `odd` (1011), parity = 1 when # of 1s in the word is `even` (1010))
```Python
result = 0
while x:
    result ^= x & 1 #XOR
    x >> = 1
```
- Explain `result ^= x & 1`
    - If res is even (0) and x-bit is 1, res evaluates to odd (1).
    - If res is odd (1) and x-bit is 1, res evaluates to even (0).
### 1.2.2. LeetCode Questions:
- [Convert Binary Number to Integer](./solution/1290_convert_Binary_to_Integer.js) For ex: LinkedList of Binary: 1 -> 0 -> 1 = 5 in decimal
    - Tips: Bitwise operation 
        -  initialise an integer variable num to 0
        - `num << 1` left shift `num` by 1 position to make way for the val in the next node in linked list. This is same as multiplying num by 2
        - `num << 1 | head.val` Add (|) next bit to num at least significant position

## 1.3. Strings and Numbers
### 1.3.1. String and Number LeetCode Questions
| Problems   |Difficulty|      Solutions       |  Description |
|------------|:--------:|:--------------------:|:------------|
| [1. Two Sum](https://leetcode.com/problems/two-sum/)|`Easy`|[Code](./solution/1_Two_Sum.java)| Using Hash Map |
| [6. ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion/)|`Medium`|[Code](./solution/6_Zig_Zag_Conversion.py)| to identify the pattern |
| [8. String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)|`Medium`| [Code](./solution/8_String_to_Integer.py) | to solve one by one, starting with `whitespace`, then `-/+` then `numbers` by iterating through the string with O(n)|
|[125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)||[Code](./solution/125_Valid_Palindrome.py)| Check if original & reverse string are the same (ie: return *result == result[ : : -1])*|
| [167. Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum/)||[Code](./solution/167_Two_Sum_II_Input_array_is_sorted.java)| Using 2 pointers |
| [344. Reverse String](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)||[Code](./solution/344_Reverse_String.py) | 2-pointer approach to reverse the string without creating extra memory (i.e: Space Complexity O(1)|
| [441. Arranging Coins](https://leetcode.com/problems/arranging-coins/)| | [Code](./solution/441_Arranging_Coins.py) | Using Mathematics Formula |
| [454. 4Sum II](https://leetcode.com/problems/4sum-ii/)||[Code](./solution/454_4Sum_II.java)| Using Hash Map |
|[1446. Consecutive Characters](https://leetcode.com/problems/consecutive-characters/)||[Code](./solution/1446_Consecutive_Characters.js)|2-pointer approach|
| [1539. Kth Missing Positive Number](https://leetcode.com/problems/kth-missing-positive-number/)|`Easy`|[Code](./solution/1539_Kth_Missing_Positive_Number.py)||

### 1.3.2. String and Number Problems 
- [728. Self Dividing Numbers](./solution/728_Self_Dividing_Numbers.py)
    - **Learn #1**: Splitting A Number (169) into Digit (9, 6, 1)
    ```Python
     while n > 0:
       d = n%10
       #Do somthing here with each digit d
       n //=10
    ```
- [1304. Find N Unique Integers Sum up to Zero](./solution/1304_Find_N_Unique_Integers_Sum_up_to_Zero.py)
    - **Learn #1**: Do not be misleading by Examples, find the general rule
    - **Learn #2**: Python to append multiple items into list: `result+=[i, -i]`

- [1370. Increasing Decreasing String](./solution/1370_Increasing_Decreasing_String.py)
    - **Learn #1**: Hash Table + Sorted + Flag `desc` to toggle the sort direction `sorted(dict, reverse = desc)`
    - **Learn #2**: To flipping between `True/False` in Python, we can use `~` i.e `desc = ~desc
- [1436. Destination City](./solution/1436_Destination_City.py)
    - **Learn**: using Hash Table to check for existing of elements instead of looping through 
- [1464. Maximum Product of Two Elements in an Array](./solution/1464_Maximum_Product_of_Two_Elements_in_an_Array.py)
Given the array of integers `nums`, you will choose two different indices i and j of that array. Return the maximum value of `(nums[i]-1)*(nums[j]-1)`.
    - **Learn**: Find the 2 largest elements in nums
- [1748. Sum of Unique Elements](./solution/1748_Sum_of_Unique_Elements.py)
    - **Learn**: Using Hash Table to calculate Unique Element (like below code), we can use `collections.Counter(nums)`
    ```Python
          for num in nums:
            if num in dict:
                dict[num]+=1
            else:
                dict[num]=1
    ```
# 2. Arrays
## 2.1. Keynotes
- To insert First Element to Array: `list.insert(0,new_element)` (Exercise: 66)

| Operation  |Complexity|Description|
|------------|:--------:|-----------|
|Retrieve       |`O(1)` ||
|Update         |`O(1)` ||
|Append         |`O(1)` |Append (Inserrt to full array) can be handled by `resizing`, i.e: allocating a new array with addtional memory and copying over the entries from the original array.<br>However, the average time for insertion is constant as `resizing` is very infrequent.|
|Insert @ ith index|`O(n-i)`| Use to insert First Element to array `list.insert(0,new_element)` |
|Delete @ ith index|`O(n-i)`| Delete an element @ ith from an array requires moving all successive elements on over to the left to fill the vacated @ ith|

## 2.2. Array Problems

- [75. Sort Colors (Dutch National Flag Problem)](./solution/75_Sort_Colors.py)
    - **Learn #1**: to sort an array with (3 type of element) in Time Complexity O(n), use `Dutch National Flag` algo.
      - Select pivot as a middle number, say array contains [0,1,2], choose `pivot=1`
      - First iteration: go Left to right, move `element` < `pivot` to left
      - Second iteration: go Right to left, move `element` > `pivot` to right, stop when meeting `element` < `pivot`.

| Problems   |Difficulty|      Solutions       |  Description |
|------------|:--------:|:--------------------:|:------------|
| [66. Plus One](https://leetcode.com/problems/plus-one/)| `Easy` |[Code](./solution/66_Plus_One.py)| Using `list.insert(0,new_element)` for first element insert to array|

# 3. Linked List
## 3.1. Keynotes
- Create a linked list with `dummy_head` and `tail`: `dummy_head = tail = ListNode()` using `tail` to move (Exercise: 21)

## 3.2. Linked List Problems

| Problems   | Difficulty |     Solutions      |  Description |
|----------  |:----------:|:------------------:|:-------------|
|[21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)|`Easy`|[Code](./solution/21_Merge_Two_Sorted_List.py)| Use 2 pointers to traverse the two lists|


# Part B: Algorithms

### Searching
| Algo Name   |      Note      | 
|----------|:-------------:|
|[Breadth First Search (BFS)](/algorithm/searching/breadthFirstSearch.js)| Shortest Path; Closer Nodes|


# LeetCode Solutions

- [1299. Replace Elements with Greatest Element on Right Side](./solution/1299_Replace_Elements_with_Greatest_Element_on_Right_Side.py)
    - **Learn #1**: Look at the problem from Right to Left
    ```Python
    Tradition: arr = [17,18,5,4,6,1] > [18, , , , , , ]          > [18,6, , , , , ]
    Optimal  : arr = [17,18,5,4,6,1] > [, , , , , , -1] curMax=1 > [, , , , , 1,-1] curMax=6
    ```

### 2D Matrix
- [1351. Count Negative Numbers in a Sorted Matrix](./solution/1351_Count_Negative_Numbers_in_a_Sorted_Matrix.py)
    - **Learn #1**: `O(n+m)` 2D Array => Using 2-Pointer Approach => "trace" the outline of the staircase 
    - **Learn #2**: `Q(m*log(n))` Sorted Array => Binary Search Tree: to search to position of First Negative Number in the Array
    ```Python
     def binarySearch(row):
            start = 0
            end = len(row) - 1
            
            while (start <= end):
                # Mid post 
                mid = start + (end - start)//2
                if (row[mid] < 0):
                    end = mid - 1
                else:
                    start = mid + 1
            
            return len(row) - start
    ```

### Linked List


### Binary Tree
#### General Tips for Tree:
- **Learn #1**: Search Types
    -  BFS : While ? Because using Recursion costs additional Space Complexity due to Recusive call in Stack
    -  DFS : Recursion
- **Learn #2**: Traversal Type
    - Pre-Order: Root - Left - Right
    - In-Order : Left - Root - Right
    - Post-Order: Left - Right - Root
- BFS Pseudo Code:
```Python
def bfs(root):
    res = []
    queue = [root]
    while(queue):
        node = queue.pop(0) #pop(0) = dequeue
        if node:
            res.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
```

- DFS Pseudo Code:
```Python
def dfs_postOrder(root, res):
    if (root):
        dfs_postOrder(root.left)
        dfs_postOrder(root.right)
        res.append(root.val)

dfs_postOrder(root, [])   
```


| Problems   |      Solutions      |  Description |
|----------|:-------------:|:------|
|104. Maximum Depth of Binary Tree|[Code](./solution/104_Maximum_Depth_of_Binary_Tree.java) | DFS|
| [107. Binary Tree Level Order Traversal II](https://leetcode.com/problems/reverse-string/)|[Code](./solution/107_Binary_Tree_Level_Order_Traversal_II.py) | BFS + Each Tree Level Traversal <br> <img src="https://user-images.githubusercontent.com/64508435/89198914-71fcb980-d5e0-11ea-9f4b-77ae4364bd1b.JPG" width="500" />|

[617. Merge Two Binary Trees](./solution/617_Merge_Two_Binary_Trees.py)
- **Learn #1**: Using [Recursion](https://www.youtube.com/watch?v=p3vVYNngyxs). Identify the base cases

[897. Increasing Order Search Tree](./solution/897_Increasing_Order_Search_Tree.py)
- **Learn #1**: Tracing through the entire tree using Current Node: `curr = tree`
```Python
tree = TreeNode(val = val_list.pop(0))
curr = tree

for i in range(0, len(val_list)):
    val = val_list[i]
    curr.right = TreeNode(val=val)
    curr = curr.right
```
[938. Range Sum of BST](./solution/938_Range_Sum_of_BST.py)
- **Learn #1**: Using the property of BST
```Python
if node.val < low:
   queue.append(node.right)
elif node.val > high:
   queue.append(node.left)
```

[1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree](./solution/1379_Find_Corresponding_Node_of_a_Binary_Tree_in_a_Clone_of_That_Tree.py)
- BFS Implementation in Python: using `pop(0)` for dequeue and `append` for enqueue
```Python
queue = [cloned]
while(queue):
    node = queue.pop(0) #pop(0) = dequeue
    if node:
        if node.val == t:
            return node
        queue.append(node.left)
        queue.append(node.right)
```
[(Back to top)](#table-of-contents)

### N ary Tree
[590. N-ary Tree Postorder Traversal](./solution/590_Nary_Tree_Postorder_Traversal.py)

- **Learn #1**: DFS expansion for N-ary tree
```Python
def dfs_postOrder(root, result):
    if (root):
        for child in root.children:
            dfs_postOrder(child, result)
        result.append(root.val)
```

### Class Design
[1603. Design Parking System](./solution/1603_Design_Parking_System.py)
- **Learn #1**: How to use Hash Table to look up the value
```Python
def __init__(self, big: int, medium: int, small: int):
        self.lots = {3: small, 2: medium, 1: big}

    def addCar(self, carType: int) -> bool:
        lot = self.lots[carType]
```

### Others

[(Back to top)](#table-of-contents)



# Resources
[Data Structure & Algo - TypeScript](https://github.com/CoffeelessProgrammer/Data-Structures-and-Algorithms-TS)


[(Back to top)](#table-of-contents)

# License
© Copyright by CodeXplore ☞ Do not Reup <br>
[(Back to top)](#table-of-contents)


