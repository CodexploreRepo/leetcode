class Solution:
    def isValidBST(self, root: Optional[TreeNode], low=float("-inf"), high=float("inf")) -> bool:
        #Base Case: If this is None node > Return True
        if not root:
            return True
        else:
            #Recursive Case: if the node is not None, we will compare the node.val with Low & High Vals
            val = root.val
            if val <= low or val >= high:
                return False #if not low <= val <= high, then return False
            else:
                #If Match the condition => Recursively call the left and right sub-tree of this node
                return self.isValidBST(root.right, val, high) and self.isValidBST(root.left, low, val) 
