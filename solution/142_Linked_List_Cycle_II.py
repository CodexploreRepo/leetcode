"""
Consider the following linked list, where E is the cylce entry and X, the crossing point of fast and slow.
        D: distance from head to cycle entry E
        K: distance from E to X
        C: Length of the cycle
                          _____
                         /     \
        head_____D______E       \
                        \       /
                         X_____/   
        
    
        If fast and slow both start at head, when fast catches slow, slow has traveled s and fast f = 2s. 
        s = D + K + iC
        f = D + K + jC
        Since f = 2s => D + K = C(j-2i)
        
        For simplication, take i = 0 (i.e: Slow do not travel in cycle), D + K = Cj => D = Cj - K 
  
        Thus if two pointers start from P1 @ head and P2 @ X (+K step away from E), respectively, 
        once P1 reaches E (travelled D), the P2 also reaches E (travelled Cj - K and start at +K). 
        
        Idea: to move P1 (@ head) and P2 (@ meeting point of fast and slow, which is +K step away from E), once P1 meets P2, this is the starting point.
 
"""


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                p1 = head 
                p2 = slow # +k step away from E
                while p1 != p2:
                    p1 = p1.next
                    p2 = p2.next
                return p1
        return None
        
