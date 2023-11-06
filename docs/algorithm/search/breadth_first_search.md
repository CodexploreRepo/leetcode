# Breadth-first search (BFS)

## 3.1. BFS for Tree Level Order Traversal

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

## 3.1. BFS for Graph

- **BFS for Graph**: need to keep track on `visited = set()` vertices
- **BFS to find shortest path** for _un-weighted_ graph or _weighted graph if all costs are equal_, we can use BFS (Level Traversal) instead of Dijkstra's algorithm.
- **Find Neighbors:**
  - **2D Matrix**:
  ```Python
  direction = [(0,-1), (0,1), (-1,0), (1,0)] #Top, Down, Left, Right
  while(queue):
      i, j = queue.pop(0)
      for d_i, d_j in direction:
          new_i, new_j = i + d_i, j + d_j
          if (new_i >= 0 and new_i < row) and (new_j >= 0 and new_j < col):
          #For valid new_i, new_j, do something
  ```
