class Solution:
    def isValidBST(self, root: Optional[TreeNode], l=float("-inf"), r = float("inf")) -> bool:
        if (root):
            if l < root.val < r:
                #If Match the condition => Recursively call the left and right sub-tree of this node
                return self.isValidBST(root.left, l, root.val) and self.isValidBST(root.right, root.val, r)
            else:
                return False #if not low <= val <= high, then return False
        else:
            return True  #Base Case: If this is None node > Return True
        
