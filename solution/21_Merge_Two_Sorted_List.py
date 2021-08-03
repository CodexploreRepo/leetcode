# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #dummy_head to keep track the head of the result linked list
        #tail to keep track the end of the result linked list
        
        """
        Time Complexity: O(n+m)
        Space: O(1) as re-use existing nodes
        """
        dummy_head = tail = ListNode()
        while (l1 and l2):
            if l1.val < l2.val:
                tail.next, l1 = l1, l1.next
            else:
                tail.next, l2 = l2, l2.next
            tail = tail.next
        
        if l1: tail.next = l1
        if l2: tail.next = l2
        
        return dummy_head.next #as the init dummy_head.val = 0
