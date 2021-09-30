class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        curA, curB = headA, headB
        lenA, lenB = 1,1
        while (curA.next):
            curA = curA.next
            lenA+=1
        while(curB.next):
            curB = curB.next
            lenB+=1
        if curA == curB:
            if lenA > lenB:
                diff = lenA - lenB
                for _ in range(diff):
                    headA = headA.next
            else:
                diff = lenB - lenA
                for _ in range(diff):
                    headB = headB.next

            while (headA != headB and headA and headB):
                headA = headA.next
                headB = headB.next
            return headA
                
                    
