class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        head = 1 -> 2 -> 3 -> 4 -> 5
               1 <- 2 <- 3 <- 4 <- 5 = head
        Time: O(n)
        Space: O(1)
        """
        curr = None
        while(head):
            temp = head.next
            head.next = curr
            curr = head
            head = temp
        return curr
