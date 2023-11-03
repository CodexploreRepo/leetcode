# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # to create a reference to the result
        dummy_head = tail = ListNode()
        # to ensure that both l1 and l2 is not None
        while (l1 and l2):
            if l1.val >= l2.val:
                tail.next = l2
                l2 = l2.next
            else:
                tail.next = l1
                l1 = l1.next

            tail = tail.next
        
        if l1: tail.next = l1
        if l2: tail.next = l2

        return dummy_head.next
        
