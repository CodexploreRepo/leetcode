class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        queue = [root]
        while(queue):
            size, prev = len(queue), Node()
            for _ in range(size):
                cur = queue.pop(0)
                if _ != size: #to ensure that if the last node, no need to update the .next
                    prev.next = cur
                    prev = cur
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
        return root
