class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        else:
            if p and q:
                if p.val != q.val:
                    return False
                else:
                    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
                return False
                
