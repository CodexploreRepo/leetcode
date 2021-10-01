# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        m = 0
        head = curr = ListNode(0)
        while(l1 and l2):
            curr_sum = l1.val + l2.val + m
            m = curr_sum//10
            curr.next = ListNode(curr_sum % 10)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next

        if l1 or l2:
            l = l1 if l1 else l2
            while(l):
                curr_sum = l.val + m
                m = curr_sum//10
                curr.next = ListNode(curr_sum % 10)
                curr = curr.next
                l = l.next
        if m != 0:
            curr.next = ListNode(m)
            curr = curr.next
        
        return head.next
        
