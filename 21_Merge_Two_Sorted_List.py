# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #Head to keep track the head of the result linked list
        #Tail to keep track the end of the result linked list
        head = tail = ListNode(-1)
        while(l1 and l2):
            #print(l1.val, l2.val)
            if (l1.val > l2.val):
                tail.next = l2
                l2 = l2.next
            else:
                tail.next = l1
                l1 = l1.next
            tail = tail.next
         
        
        if l1: tail.next = l1
        if l2: tail.next = l2
        
        
        return head.next
