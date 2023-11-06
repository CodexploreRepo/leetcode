# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        lh = self.calHeight(root.left)
        rh = self.calHeight(root.right)
        # check the current left & right substrees and ensure each sub-stree is also balanced
        return (
            abs(lh - rh) <= 1
            and self.isBalanced(root.left)
            and self.isBalanced(root.right)
        )

    def calHeight(self, root):
        if not root:
            return 0
        else:
            return (
                max(self.calHeight(root.left), self.calHeight(root.right)) + 1
            )
