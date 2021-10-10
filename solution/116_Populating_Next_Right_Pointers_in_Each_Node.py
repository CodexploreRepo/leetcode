class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        queue = [root]
        while(queue):
            size, prev = len(queue), Node() #at the start of each level, need to init an empty node "prev", as prev will store the previous node
            for _ in range(size):
                cur = queue.pop(0)
                prev.next = cur
                prev = cur
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
        return root
    
    
