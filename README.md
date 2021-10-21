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
- [4. Hash Map](#4-hash-map)
  - [4.1. Keynotes](#41-keynotes)
- [5. Queue](#5-queue)
- [Part B: Algorithms](#part-b-algorithms)
- [1. Recursion](#1-recursion)
- [2. Dynamic Programming](#2-dynamic-programming)
- [3. BFS](#3-bfs)
- [4. Graph Theory](#4-graph-theory)
  - [4.1. Topological Sort](#41-topological-sort)
  - [4.2. Minimum Spanning Tree - Kruskal Algorithm](#42-minium-spanning-tree-kruskal-algorithm)
  - [4.3. Minimum Spanning Tree - Prim Algorithm](#43-minium-spanning-tree-prim-algorithm)
  - [4.4. Shortest Path for Weighted Graph - Dijkstra Algorithm](#44-shortest-path-dijkstra-algorithm)
- [Searching](#searching)
- [LeetCode Solutions](#leetcode-solutions)
    - [Binary Tree - BFS & DFS](#binary-tree)
    - [N-ary Tree - BFS & DFS](#n-ary-tree)
    - [Class Design](#class-design)
    - [Others](#others)
- [Resources](#resources)
- [License](#license)

# Part A: Data Structure
# 1. Primitive Types
## 1.1. KeyNotes

- [Number] **Infinity**: `float('inf')` and `float('-inf')`
- [Number] Math Operator: `%10` modulus 10 to extract last digit in a number, `//10` to remove the last digit in a number
- [Number > String] 9 to "9": `char(ord('0') + 9)`
- [String > Number] "9" to 9: `ord('9') - ord('0') = 9`, for s="123" to 123: `res = res*10 + ord(s[i]) - ord('0')`
- [String] Palindromic `all(s[i] == s[~i] for i in range(len(s//2))` where `s[~i] = s[-(i+1)]`
- [Set] Create a set of digits `['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']` => `nums = set('0123456789')`
- [Circular Array] to circular the array index `index = (index + 1) % array_size`

### External Library:
-  `help()`: to understand the function usage. For ex: `help(math.log)`
-  `dir()`: See all the names in `module` or to understand an un-known object, using the built-in function  **dir()**
```Python
import math
print(dir(math))

['__doc__', '__file__',....]
```

## 1.2. Bitwise Operation:
- `n-bit`binary numbers can re-present 2^(n) distinct integers. For example: 4-bit binary numbers can represent 16 distinct integers. 
- 
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
#### 1.3.1. find() and rfind()
- `.find()`: find the starting index of the first occurrence of a substring as specified
<img width="845" alt="Screenshot 2021-08-25 at 22 11 40" src="https://user-images.githubusercontent.com/64508435/130806533-e176d08a-168c-4b26-92d2-6b0dacb1aa4a.png">

```python
s = 'machine learning'

s.find('n') #return = 5 > find the first occurance 'n'
s.find('n', 6) #return = 12 >  find the occurance from 6th index
s.find('n', 6, 10) #return = -1 > represents not found, not a negative index here
```
- `.rfind()`: find the starting index in the reverse direction
```Python

s.rfind('n') #return = 5 > find the first occurance 'n'
s.rfind('n', 15) #return = -1 >  If a second argument is provided, it is where the search ends in the reverse direction, inclusive of this index itself
s.rfind('n', 0, 12) #return = 5 > represents not found, not a negative index here
```
### String Format
- Padding 0: For example, convert integer **month = 2 to "02"**: f"{month:02d}"

### 1.3.3. String and Number LeetCode Questions
| Problems   |Difficulty|      Solutions       |  Description |
|------------|:--------:|:--------------------:|:------------|
| [1. Two Sum](https://leetcode.com/problems/two-sum/)|`Easy`|[Code](./solution/1_Two_Sum.java)| Using Hash Map |
| 2. Add Two Number|`Medium`|[Code](./solution/2_Add_Two_Numbers.py)| |
| 3. Longest Substring Without Repeating Characters|`Medium`|[Code](./solution/3_Longest_Substring_Without_Repeating_Characters.py)| Need to have a start pointer along with i to loop through each element and a hash table to store the location |
| 5. Longest Palindromic Substring |`Medium`|[Code](./solution/5_Longest_Palindromic_Substring.py)| Need to check if odd pal `cabac` and even pal `abba` and keep track on the maximum|
| [6. ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion/)|`Medium`|[Code](./solution/6_Zig_Zag_Conversion.py)| to identify the pattern |
| [8. String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)|`Medium`| [Code](./solution/8_String_to_Integer.py) | to solve one by one, starting with `whitespace`, then `-/+` then `numbers` by iterating through the string with O(n)|
| 15. 3Sum |`Medium`| [Code](./solution/15_3Sum.py) | |
| 17. Letter Combinations of a Phone Number |`Medium`| [Code](./solution/17_Letter_Combinations_of_a_Phone_Number.py) | Using the recursion |
| 20. Valid Parentheses | `Easy`| [Code](.solution/20_Valid_Parentheses.py)| Using Stack|
| [50. Pow(x, n)](https://leetcode.com/problems/powx-n/)|`Medium`| [Code](./solution/50_Pow_x_n.py) | Using Recursive Approach, divide `power n` by `//2`, remember to take care of negative power i.e `n < 0` |
|[125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)||[Code](./solution/125_Valid_Palindrome.py)| Check if original & reverse string are the same (ie: return *result == result[ : : -1])*|
| [167. Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum/)||[Code](./solution/167_Two_Sum_II_Input_array_is_sorted.java)| Using 2 pointers |
| [344. Reverse String](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)||[Code](./solution/344_Reverse_String.py) | 2-pointer approach to reverse the string without creating extra memory (i.e: Space Complexity O(1)|
| [441. Arranging Coins](https://leetcode.com/problems/arranging-coins/)| | [Code](./solution/441_Arranging_Coins.py) | Using Mathematics Formula |
| [454. 4Sum II](https://leetcode.com/problems/4sum-ii/)||[Code](./solution/454_4Sum_II.java)| Using Hash Map |
|[1446. Consecutive Characters](https://leetcode.com/problems/consecutive-characters/)||[Code](./solution/1446_Consecutive_Characters.js)|2-pointer approach|
| [1539. Kth Missing Positive Number](https://leetcode.com/problems/kth-missing-positive-number/)|`Easy`|[Code](./solution/1539_Kth_Missing_Positive_Number.py)||

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
- To reverse List: `list[::-1]`
- To sort a list: `list.sort(reverse = True)`
- To insert First Element to Array: `list.insert(0,new_element)` (Exercise: 66)
- To insert @ Tail: `list.append(element)`
- To insert Many @ Tail: `list.append([1,2,3])`
- To remove:
```Python
l = [1, 2, 3, 5, 7, 9, 11, 13, 15, 17, 19, 23, 29, 31, 37, 41, 43, 47, 49]

#.remove(): remove a specific value
# l.remove(4) # error if remove 4 as 4 not in l
l.remove(9)   # l = [1, 2, 3, 5, 7, 11, 13, 15, 17, 19, 23, 29, 31, 37, 41, 43, 47, 49]

#.pop(): remove at an index and return
l.pop()  # return 49 and l = [1, 2, 3, 5, 7, 11, 13, 15, 17, 19, 23, 29, 31, 37, 41, 43, 47]
l.pop(1) # return 2 and  l = [1, 3, 5, 7, 11, 13, 15, 17, 19, 23, 29, 31, 37, 41, 43, 47] 

#.clear(): remove all
l.clear # l = []
```
- To iterate both index and value in List: `enumerate`
```Python
for index, value in enumerate(arr):
  print(index, value)
0 a
1 b
2 c
```

| Operation  |Complexity|Description|
|------------|:--------:|-----------|
|Retrieve       |`O(1)` ||
|Update         |`O(1)` ||
|Append         |`O(1)` |Append (Inserrt to full array) can be handled by `resizing`, i.e: allocating a new array with addtional memory and copying over the entries from the original array.<br>However, the average time for insertion is constant as `resizing` is very infrequent.|
|Insert @ ith index|`O(n-i)`| Use to insert First Element to array `list.insert(0,new_element)` |
|Delete @ ith index|`O(n-i)`| Delete an element @ ith from an array requires moving all successive elements on over to the left to fill the vacated @ ith|

## 2.2. Array Problems
### 2.2.1. 1D Array

| Problems   |Difficulty|      Solutions       |  Description |
|------------|:--------:|:--------------------:|:------------|
| 11. Container With Most Water |`Medium`|[Code](./solution/11_Container_With_Most_Water.py)| Need to start from both 2 end and go inwards |
| [66. Plus One](https://leetcode.com/problems/plus-one/)| `Easy` |[Code](./solution/66_Plus_One.py)| Using `list.insert(0,new_element)` for first element insert to array|
| 121. Best Time to Buy and Sell Stock|`Easy`|[Code](./solution/121_Best_Time_to_Buy_and_Sell_Stock.py)| Need to keep track on buy price with the next days|
- [75. Sort Colors (Dutch National Flag Problem)](./solution/75_Sort_Colors.py)
    - **Learn #1**: to sort an array with (3 type of element) in Time Complexity O(n), use `Dutch National Flag` algo.
      - Select pivot as a middle number, say array contains [0,1,2], choose `pivot=1`
      - First iteration: go Left to right, move `element` < `pivot` to left
      - Second iteration: go Right to left, move `element` > `pivot` to right, stop when meeting `element` < `pivot`.
- [1299. Replace Elements with Greatest Element on Right Side](./solution/1299_Replace_Elements_with_Greatest_Element_on_Right_Side.py)
    - **Learn #1**: Look at the problem from Right to Left
    ```Python
    Tradition: arr = [17,18,5,4,6,1] > [18, , , , , , ]          > [18,6, , , , , ]
    Optimal  : arr = [17,18,5,4,6,1] > [, , , , , , -1] curMax=1 > [, , , , , 1,-1] curMax=6
    ```

### 2.2.2. 2D Matrix
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

# 3. Linked List
## 3.1. Keynotes
- Create a linked list with `dummy_head` and `tail`: `dummy_head = tail = ListNode()` using `tail` to move (Exercise: 21)
- Create a `dummy_head = None` for the case do NOT require extra node.
## 3.2. Linked List Problems

| Problems   | Difficulty |     Solutions      |  Description |
|----------  |:----------:|:------------------:|:-------------|
|19. Remove Nth Node From End of Lists|`Medium`|[Code](./solution/19_Remove_Nth_Node_From_End_of_List.py)||
|[21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)|`Easy`|[Code](./solution/21_Merge_Two_Sorted_List.py)| Use 2 pointers to traverse the two lists|
|[92. Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/)|`Medium`|[Code](./solution/92_Reverse_Linked_List_II.py)| |
|[141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)|`Easy`|[Code](./solution/141_Linked_List_Cycle.py)| **Floyd's Tortoise and Hare Algorithm**: Use 2 pointers slow fast to traverse, if slow meets fast, meaning it is a cycle linked list|
|[142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)|`Medium`|[Code](./solution/142_Linked_List_Cycle_II.py)| 	:star: **Good Algo to do** Need to calculate the distance to reach |
|160. Intersection of Two Linked Lists|`Easy`|[Code](./solution/92_Reverse_Linked_List_II.py)|Please refer the comment|
|[206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)|`Easy`|[Code](./solution/92_Reverse_Linked_List_II.py)||

# 4. Hash Map
## 4.1. Keynotes
- `len(d)`: return numbers of items in dictionary
- `d[key]` or `d.get(key, default_value)`: return corresponding value with specific key, return *default_value* when key is not found
- `in` or `not in`: **membership operators** 
- `d.pop(key)` or `del d[key]`: remove an item from the dictionary 
To access keys, values, and items
- `d.keys()` return the set of all keys in dictionary d
- `d.values()` return the set of all values in dictionary d
- `d.items()` return the set of all items (pair of keys and values) in dictionary d
```Python
#to access both keys and values
for k, v in d.items():
    print(k, v)
```

# 5. Queue
- Queue will be used for BFS
- Queue in Python: using list with **dequeue** `list.pop(0)` (But requiring O(n) as need to shift all elements) time and **enqueue** `list.append(item)`
- Queue with Built-in Function:
```Python
from collections import deque
q = deque() # Initializing a queue
q.append('a') # Adding elements to a queue
# Removing elements from a queue - only O(1) in compare with using List to implement Queue
q.popleft()
```
| Problems   | Difficulty |     Solutions      |  Description |
|----------  |:----------:|:------------------:|:-------------|
|622. Design Circular Queue|`Medium`|[Code](./solution/622_Design_Circular_Queue.py)|To circular the array: `self.tail = (self.tail + 1)%self.size` For enqueue, need to take care only the tail, for dequeue, need to take care only the head. Please refer the link for the circular queue example https://leetcode.com/explore/learn/card/queue-stack/228/first-in-first-out-data-structure/1396/|

# Part B: Algorithms
# 1. Recursion
- **Key Points**: Change Large Input &#8594; Smaller Input
  - Ex1 - [Fibonacci](https://www.mathsisfun.com/numbers/fibonacci-sequence.html): The next number is found by adding up the two numbers before it
    - `fib(1) = fib(2) = 1`
    - `fib(n) = fib(n-1) + fib(n-2)`

# 2. Dynamic Programming
- **Tips**: For Dynamic Programming, it s very important to write down the `recurrence relationship` like below
  - `d(i,j)` cell = relationship with its neighbors: `d(i, j+1)`, `d(i+1, j)`, `d(i+1, j+1)`
<img width="545" src="https://user-images.githubusercontent.com/64508435/138033528-43884ee0-9cf9-438b-9c6e-732d9f63e758.png">

- **Key Points**: DP can be done either by `Recursive (Top-Down)` or `Iterative (Bottom-Up)` Approach
- **Key Points**: Cache `memo` can be passed into the function as an input param
```Python
    def climbStairs(self, n: int, memo = {1: 1, 2:2}) -> int:
        if n not in memo: #T(n) = T(n-1) + T(n-2)
            memo[n] = self.climbStairs(n-1, memo) + self.climbStairs(n-2, memo) 
        return memo[n]
```
| Problems   |      Solutions      |  Difficulty |Description |
|------------|:-------------------:|-------------|------------|
|70. Climbing Stairs |[Code](./solution/70_Climbing_Stairs.py)| `Easy`|At T(n): first step = 1, remaining steps = T(n-1) or first step = 2, remaing steps = T(n-2). This recurrence relationship is similar to Fibonacci number|
|72. Edit Distance |[Code](./solution/72_Edit_Distance.py)| `Hard`||
|1143. Longest Common Subsequence |[Code](./solution/1143_Longest_Common_Subsequence.py)| `Medium`||

# 3. BFS
- **BFS for Graph**: need to keep track on `visited` vertices
- **BFS to find shortest path** for *un-weighted* graph or *weighted graph if all costs are equal*, we can use BFS (Level Traversal) instead of Dijkstra's algorithm.

| Problems   | Type        |      Solutions      |  Difficulty   | Description |
|------------|:-----------:|:-------------------:|:-------------:|------------|
|200. Number of Islands | **Graph** |[Code](./solution/200_Number_of_Islands.py)| `Medium`| Need to search the adjacent location (top, down, left, right) of the "1" cell to find the maximum size of an island, then can continue|
|429. N-ary Tree Level Order Traversal|**Tree** |[Code](./solution/429_N-ary_Tree_Level_Order_Traversal.py)| `Medium`| |
|752. Open the Lock |**Graph** |[Code](./solution/752_Open_the_Lock.py)| `Medium`| from start, add the next possible turn into the queue and then continue to search with Target|
|2039. The Time When the Network Becomes Idle |**Graph** |[Code](./solution/2039_The_Time_When_the_Network_Becomes_Idle.py)| `Medium`| We can use DFS to calculate the travel time from master server to remain data servers like Level Traversal|

# 4. Graph Theory
## 4.1. Topological Sort
| Problems   |      Solutions      |  Difficulty |Description |
|------------|:-------------------:|-------------|------------|
|210. Course Schedule II |[Code](./solution/210_Course_Schedule_II.py)| `Medium`| Step 1: Conver into a graph, then apply Topological Sort, remember to add the flag for Cycle Detection|

## 4.2. Minimum Spanning Tree - Kruskal Algorithm
| Problems   |      Solutions      |  Difficulty |Description |
|------------|:-------------------:|-------------|------------|
|1584. Min Cost to Connect All Points |[Code](./solution/1584_Min_Cost_to_Connect_All_Points.py)| `Medium`| Using Kruskal Algorithm|


## 4.3. Minimum Spanning Tree - Prim Algorithm
| Problems   |      Solutions      |  Difficulty |Description |
|------------|:-------------------:|-------------|------------|
|1584. Min Cost to Connect All Points |[Code](./solution/1584_Min_Cost_to_Connect_All_Points.py)| `Medium`| Using Prim Algorithm|

## 4.4. Shortest Path for Weighted Graph - Dijkstra Algorithm
- Dijkstra's algorithm: find the shortest path like BFS, but for weighted graphs.
- If all costs are equal, we can use BFS (Level Traversal) instead of Dijkstra's algorithm.

| Problems   |      Solutions      |  Difficulty |Description |
|------------|:-------------------:|-------------|------------|
|743. Network Delay Time |[Code](./solution/743_Network_Delay_Time.py)| `Medium`| This is Dijkstra for the directed Graph - Need to take care the adj_list |

### Searching
| Algo Name   |      Note      | 
|----------|:-------------:|
|[Breadth First Search (BFS)](/algorithm/searching/breadthFirstSearch.js)| Shortest Path; Closer Nodes|


# LeetCode Solutions

### Binary Tree
#### General Tips for Tree:
- **Learn #1**: Search Types
    -  BFS : While ? Because using Recursion costs additional Space Complexity due to Recusive call in Stack
    -  DFS : Recursion

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


| Problems   |      Solutions      |  Difficulty |Description |
|------------|:-------------------:|-------------|------------|
|98. Validate Binary Search Tree |[Code](./solution/98_Validate_Binary_Search_Tree.py)| `Medium`|Recursion: check one by one node to ensure that low < node.val < hight. Why low & high ? because we need to ensure the left and right child to be within the range|
|100. Same Tree |[Code](./solution/100_Same_Tree.py)| `Easy`|Recursion: Compare 2 root, then recusively compare both left with left and right with right sub-tree|
|101. Symmetric Tree |[Code](./solution/101_Symmetric_Tree.py)| `Easy`|Recursion: Call a recursive function on left and right Sub-trees|
|104. Maximum Depth of Binary Tree|[Code](./solution/104_Maximum_Depth_of_Binary_Tree.java)| | DFS|
| [107. Binary Tree Level Order Traversal II](https://leetcode.com/problems/reverse-string/)|[Code](./solution/107_Binary_Tree_Level_Order_Traversal_II.py)| | BFS + Each Tree Level Traversal <br> <img src="https://user-images.githubusercontent.com/64508435/89198914-71fcb980-d5e0-11ea-9f4b-77ae4364bd1b.JPG" width="500" />|
|112. Path Sum |[Code](./solution/112_Path_Sum.py)| `Easy`| Need to check at leaf node, what is the remaining sum|
|116. Populating Next Right Pointers in Each Node |[Code](./solution/116_Populating_Next_Right_Pointers_in_Each_Node.py)| `Medium`|BFS |
|543. Diameter of Binary Tree|[Code](./solution/543_Diameter_of_Binary_Tree.py)|`Easy`|Need to calculate the left and the right height of the tree, then compare left_height + right_height with the max diameter|
|700. Search in a Binary Search Tree|[Code](./solution/700_Search_in_a_Binary_Search_Tree.py)|`Easy`||
|701. Insert into a Binary Search Tree|[Code](./solution/701_Insert_into_a_Binary_Search_Tree.py)|`Medium`| Same concept as Search in BST|


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


