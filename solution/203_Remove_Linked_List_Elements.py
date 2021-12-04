# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head: return head
  
        dummy_head = ListNode(None)
        dummy_head.next = head
        
        cur = dummy_head

        while(cur.next):
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy_head.next
