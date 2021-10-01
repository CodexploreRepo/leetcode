class Solution:
    maxD = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
         if root:
            self.height(root)
            return self.maxD
    def height(self, root):
        if root:
            lh = self.height(root.left)
            rh = self.height(root.right)
            self.maxD = max(self.maxD, lh+rh)
            return max(lh, rh) + 1
        else:
            return 0
