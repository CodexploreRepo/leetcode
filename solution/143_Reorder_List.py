# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # find the middle point of the linked list
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second_half = slow.next
        slow.next = None # to break the linked list into first & second half
        # reverse the second half of the linked list
        reversed_second_half = None
        while second_half:
            tmp = second_half.next
            second_half.next = reversed_second_half
            reversed_second_half = second_half
            second_half = tmp

        first_half, second_half = head, reversed_second_half
        # merge first & second half alternatively
        while second_half:
            tmp1, tmp2 = first_half.next, second_half.next
            first_half.next = second_half
            second_half.next = tmp1
            first_half, second_half = tmp1, tmp2
