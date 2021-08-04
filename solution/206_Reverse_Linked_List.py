class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        head = 1 -> 2 -> 3 -> 4 -> 5
               1 <- 2 <- 3 <- 4 <- 5 = head
        Time: O(n)
        Space: O(1)
        """
        if not (head):
            return head
        
        dummy_head = None
        currNode = head
        while(currNode):
            temp = currNode.next
            currNode.next = dummy_head
            dummy_head = currNode
            currNode = temp
        
        return dummy_head
