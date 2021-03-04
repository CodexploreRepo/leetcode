# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if (root):
            result = self.breathFirstSearch([root], [])
            return result
        else: 
            return []
    
    def breathFirstSearch(self, queue, result):
        if (len(queue)==0):
            return result
        #Total number of node in the current level
        size = len(queue)
        #Create a list contains Nodes in current level
        currentLevel = []
        for i in range(0, size):
            #Popout the first item in the queue
            currentNode = queue.pop(0)
            #Push into the current Level List
            currentLevel.append(currentNode.val)
            
            #Append the children of currentNode to the queue, which will be next Level
            if (currentNode.left):
                queue.append(currentNode.left)
            if (currentNode.right):
                queue.append(currentNode.right)
            
        #print(currentLevel)
        result.insert(0,currentLevel)
        return self.breathFirstSearch(queue, result)
        
    
        
