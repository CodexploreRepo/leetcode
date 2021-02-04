class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        t = target.val
        queue = [cloned]
        while(queue):
            node = queue.pop(0)
            if node:
                if node.val == t:
                    return node
                queue.append(node.left)
                queue.append(node.right)
        return None
