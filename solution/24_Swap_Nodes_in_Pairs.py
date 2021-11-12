class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        First, we swap the first two nodes in the list, i.e. head and head.next;
        Then, we call the function self as swap(head.next.next) to swap the rest of the list following the first two nodes.
        Finally, we attach the returned head of the sub-list in step (2) with the two nodes swapped in step (1) to form a new linked list.
        """
        if (head and head.next):
            tmp = head.next
            head.next = self.swapPairs(tmp.next)
            tmp.next = head
            return tmp
        return head
        
