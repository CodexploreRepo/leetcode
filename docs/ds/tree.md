# Tree

## Level and Height

### Level

- If n is the **root** of T, it is at Level **0**
- If n is **not the root of T**, its level is **1 greater** than the Level of its **parent**

### Height

- Height of a tree T defined in terms of the levels of its nodes
  - If T is empty, its height is `not defined`
  - If T is not empty, its height is equal to the `maximum level of its nodes`

## Binary Tree

- A binary tree is (recursive definition)
  - An empty tree, or
  - A node with a right binary tree and a left binary tree (called left/right subtrees)
- The maximum number of children for all nodes in a binary tree: ?????

### Tree Traversal

- A Tree Data Structure can be traversed in following ways:
- **Depth First Search** (DFS)
  - Preorder Traversal
  - Inorder Traversal
  - Postorder Traversal
- **Level Order Traversal** or **Breadth First Search** (BFS)

<p align="center"><img src="../.././assets/img/tree_traversal.png"></p>

#### DFS

##### Pre-order Traversal

- Pseudo-code

```
Algorithm Preorder(tree)

1. Visit the root.
2. Traverse the left subtree, i.e., call Preorder(left->subtree)
3. Traverse the right subtree, i.e., call Preorder(right->subtree)
```

- Code Implementation:

```Python
 def preorderTraversal(root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        def preorder_dfs(curr_node):
            if curr_node:
                result.append(curr_node.val)
                preorder_dfs(curr_node.left)
                preorder_dfs(curr_node.right)
        preorder_dfs(root)
        return result
```

##### In-order Traversal

- Pseudo-code

```
Algorithm Inorder(tree)

1. Traverse the left subtree, i.e., call Inorder(left->subtree)
2. Visit the root.
3. Traverse the right subtree, i.e., call Inorder(right->subtree)
```

- Code Implementation:

```Python
def inorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    result = []

    def inorder_dfs(curr_node):
        if curr_node:
            inorder_dfs(curr_node.left)
            result.append(curr_node.val)
            inorder_dfs(curr_node.right)
    inorder_dfs(root)
    return result
```

##### Post-order Traversal

- Pseudo-code

```
Algorithm Inorder(tree)

1. Traverse the left subtree, i.e., call Inorder(left->subtree)
2. Traverse the right subtree, i.e., call Inorder(right->subtree)
3. Visit the root.
```

- Code Implementation:

```Python
def postorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    result = []

    def postorder_dfs(curr_node):
        if curr_node:
            postorder_dfs(curr_node.left)
            postorder_dfs(curr_node.right)
            result.append(curr_node.val)
    postorder_dfs(root)
    return result
```

#### Level Order Traversal (BFS)

```Python
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]] -> [[3],[9,20],[15,7]]
        """
        result = []
        if root:
            bfs_queue = [[root]]
            while len(bfs_queue) > 0:
                cur_level = bfs_queue.pop(0) # deque
                result.append([node.val for node in cur_level])

                next_level = []
                # add all the children of the node in the cur level in the queue
                for node in cur_level:
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)
                bfs_queue.append(next_level)

                if len(next_level) == 0:
                    break

        return result
```

## Binary Search Tree

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

- [Tree Patterns](https://medium.com/leetcode-patterns/leetcode-pattern-0-iterative-traversals-on-trees-d373568eb0ec)
- [Tree Iterative Traversal](https://leetcode.com/discuss/study-guide/937307/Iterative-or-Recursive-or-DFS-and-BFS-Tree-Traversal-or-In-Pre-Post-and-LevelOrder-or-Views)
