# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []

        def inorder_dfs(curr_node) -> None:
            if curr_node:
                inorder_dfs(curr_node.left)
                result.append(curr_node.val)
                inorder_dfs(curr_node.right)

        inorder_dfs(root)
        return result
