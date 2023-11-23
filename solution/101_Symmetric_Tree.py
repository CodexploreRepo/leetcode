# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        else:
            return self.checkSubTree(root.left, root.right)

    def checkSubTree(self, leftSubTree, rightSubTree):
        if (not leftSubTree) and (not rightSubTree):
            return True
        if (not leftSubTree) or (not rightSubTree):
            return False
        return (
            leftSubTree.val == rightSubTree.val
            and self.checkSubTree(leftSubTree.left, rightSubTree.right)
            and self.checkSubTree(leftSubTree.right, rightSubTree.left)
        )
