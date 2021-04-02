class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int, sum = 0) -> int:
        if not root:
            return sum
        elif root.val > high:
            sum = self.rangeSumBST(root.left, low, high)
        elif root.val < low:
            sum = self.rangeSumBST(root.right,low, high)
        else:
            sum = root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
        return sum
