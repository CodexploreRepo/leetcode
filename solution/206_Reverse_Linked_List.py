class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        head = 1 -> 2 -> 3 -> 4 -> 5
               1 <- 2 <- 3 <- 4 <- 5 = head
        Time: O(n)
        Space: O(1)
        """
        dummy_head = None

        while head:
            # use tmp to store the head.next (reference of the remaining list)
            tmp = head.next
            # point head.next to dummy_head
            head.next = dummy_head
            # move dummy_head to head
            dummy_head = head
            # re-assign head back to the tmp (reference of the remaining list)
            head = tmp
        return dummy_head