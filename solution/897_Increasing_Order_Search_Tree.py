# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        val_list = []
        
        def inorder_traversal(root):
            if root:
                inorder_traversal(root.left)
                val_list.append(root.val)
                inorder_traversal(root.right)
                
        inorder_traversal(root)
        
        new_root = TreeNode(val = val_list.pop(0))
        curr = new_root
        
        for i in range(0, len(val_list)):
            val = val_list[i]
            curr.right = TreeNode(val=val)
            curr = curr.right
        
        return new_root
