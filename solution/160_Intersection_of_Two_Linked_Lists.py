# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getLinkedListLength(self, head):
        ll_length = 0
        while(head):
            ll_length +=1
            head = head.next
        return ll_length
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA = self.getLinkedListLength(headA)
        lenB = self.getLinkedListLength(headB)
        if lenA > lenB:
            for _ in range(lenA-lenB):
                headA = headA.next
        else:
            for _ in range(lenB-lenA):
                headB = headB.next
        
        while headA != headB and (headA and headB):
            headA = headA.next
            headB = headB.next
        return headA
