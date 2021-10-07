class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target: int) -> bool:
        if root is None: #Special Case
            return False
        if not root.left and not root.right: #Base Case: at leaf node
            if target - root.val == 0: return True
            else: return False
        else:
            target-=root.val
            return self.hasPathSum(root.left, target) or self.hasPathSum(root.right, target)
