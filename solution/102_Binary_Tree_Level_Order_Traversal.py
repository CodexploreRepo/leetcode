# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if root:
            bfs_queue = [[root]]
            while len(bfs_queue) > 0:
                cur_level = bfs_queue.pop(0)  # deque
                result.append([node.val for node in cur_level])

                next_level = []
                for node in cur_level:
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)
                bfs_queue.append(next_level)

                if len(next_level) == 0:
                    break

        return result
