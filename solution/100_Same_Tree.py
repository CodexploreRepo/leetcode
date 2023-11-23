# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # case 1: both p and q is None -> True
        if (not p) and (not q):
            return True
        # case 2: either p or q is None -> False
        if (not p) or (not q):
            return False
        # case 3: both p and q is Not None -> check vals of p and q & their sub-trees
        return (
            (p.val == q.val)
            and self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )
