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
    - [Number](#number)
    - [Linked List](#linked-list)
    - [Binary Tree - BFS & DFS](#binary-tree)
    - [Others](#others)
- [Java Skills](#java-skills)
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
|[1446. Consecutive Characters](https://leetcode.com/problems/consecutive-characters/)|[Code](/1446_Consecutive_Characters.js)|2-pointer approach|


### Number

| Problems   |      Solutions      |  Tips |
|----------|:-------------:|:------|
| [1. Two Sum](https://leetcode.com/problems/two-sum/)|[Code](/1_Two_Sum.java)| Using Hash Map |
| [167. Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum/)|[Code](/167_Two_Sum_II_Input_array_is_sorted.java)| Using 2 pointers |
| [441. Arranging Coins](https://leetcode.com/problems/arranging-coins/)|  [Code](/441_Arranging_Coins.py) | Using Mathematics Formula |
| [454. 4Sum II](https://leetcode.com/problems/4sum-ii/)|[Code](/454_4Sum_II.java)| Using Hash Map |
| [1290. Convert Binary Number in a Linked List to Integer](https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/)|  [Code](/1290_convert_Binary_to_Integer.js) | Use Bit Shift |
| [1539. Kth Missing Positive Number](https://leetcode.com/problems/kth-missing-positive-number/)|[Code](/1539_Kth_Missing_Positive_Number.py)||

- [1304. Find N Unique Integers Sum up to Zero](./1304_Find_N_Unique_Integers_Sum_up_to_Zero.py)
    - **Learn #1**: Do not be misleading by Examples, find the general rule
    - **Learn #2**: Python to append multiple items into list: `result+=[i, -i]`
- [1370. Increasing Decreasing String](./1370_Increasing_Decreasing_String.py)
    - **Learn #1**: 
- [1436. Destination City](./1436_Destination_City.py)
    - **Learn**: using Hash Table to check for existing of elements instead of looping through 
- [1464. Maximum Product of Two Elements in an Array](./1464_Maximum_Product_of_Two_Elements_in_an_Array.py)
Given the array of integers `nums`, you will choose two different indices i and j of that array. Return the maximum value of `(nums[i]-1)*(nums[j]-1)`.
    - **Learn**: Find the 2 largest elements in nums
- [1748. Sum of Unique Elements](./1748_Sum_of_Unique_Elements.py)
    - **Learn**: Using Hash Table to calculate Unique Element (like below code), we can use `collections.Counter(nums)`
    ```Python
          for num in nums:
            if num in dict:
                dict[num]+=1
            else:
                dict[num]=1
    ```


### Linked List
| Problems   |      Solutions      |  Description |
|----------|:-------------:|:------|
|[21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)|[Code](/21_Merge_Two_Sorted_List.py)| Use 2 pointers: Head & Tail|


### Binary Tree

| Problems   |      Solutions      |  Description |
|----------|:-------------:|:------|
|104. Maximum Depth of Binary Tree|[Code](/104_Maximum_Depth_of_Binary_Tree.java) | DFS|
| [107. Binary Tree Level Order Traversal II](https://leetcode.com/problems/reverse-string/)|[Code](/107_Binary_Tree_Level_Order_Traversal_II.py) | BFS + Each Tree Level Traversal <br> <img src="https://user-images.githubusercontent.com/64508435/89198914-71fcb980-d5e0-11ea-9f4b-77ae4364bd1b.JPG" width="500" />|


[1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree](/1379_Find_Corresponding_Node_of_a_Binary_Tree_in_a_Clone_of_That_Tree.py)
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

### Others

[(Back to top)](#table-of-contents)

# Java Skills
## Array
### How to return an Array ?

```Java
public int[] twoSum(int[] nums, int target) {
      ...
      return new int[] {69, 123};
```
## HashMap
### Initialize a Hashmap
Method 1 (using Map interface): `Map<Integer, Integer> map = new HashMap<>();`<br>
Method 2                      : `HashMap<String, Integer> people = new HashMap<String, Integer>();`
### Put
`map.put(key, value);`
### Get
`map.get(key, value);`
### Check if Key Exists
`map.containsKey(key);`
### Loop Through Hash Map 
```Java
// Print keys
for (String i : capitalCities.keySet()) {
  System.out.println(i);
}

// Print values
for (String i : capitalCities.values()) {
  System.out.println(i);
}
```



# Resources
[Data Structure & Algo - TypeScript](https://github.com/CoffeelessProgrammer/Data-Structures-and-Algorithms-TS)


[(Back to top)](#table-of-contents)

# License
© Copyright by CodeXplore ☞ Do not Reup <br>
[(Back to top)](#table-of-contents)


