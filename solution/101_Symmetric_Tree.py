class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        else:
            return self.checkSubTree(root.left, root.right)
    
    def checkSubTree(self, leftSub, rightSub):
        if not leftSub and not rightSub:
            return True
        if leftSub and rightSub:
            if leftSub.val != rightSub.val:
                return False
            else:
                return self.checkSubTree(leftSub.left, rightSub.right) and self.checkSubTree(leftSub.right, rightSub.left)
        else: #This case: either leftSub or RightSub is None, but not all is none
            return False 
