# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while(fast and fast.next): #to ensure that we only reach to the last node
            slow = slow.next
            fast = fast.next.next

        prev = None
        while(slow):
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        left, right = head, prev
        while(right):
            if right.val != left.val:
                return False
            left = left.next
            right = right.next
        return True
        
