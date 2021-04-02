class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        
        def dfs_postOrder(root, result):
            if (root):
                for child in root.children:
                    dfs_postOrder(child, result)
                result.append(root.val)
            
        dfs_postOrder(root, result)
        return result
        
