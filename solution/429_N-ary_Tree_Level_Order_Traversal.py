class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        queue = collections.deque([root])
        res = []
        while(queue):
            size, cur_level = len(queue), []
            for _ in range(size):
                cur_node = queue.popleft()
                cur_level.append(cur_node.val)
                for child in cur_node.children:
                    if child:
                        queue.append(child)
            res.append(cur_level)
        
        return res
