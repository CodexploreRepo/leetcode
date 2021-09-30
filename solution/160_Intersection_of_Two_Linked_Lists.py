class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        curA, curB = headA, headB
        lenA, lenB = 1,1
        
        #Step 1: Traverse to the end of each linked list, and calculate the branch length
        while (curA.next):
            curA = curA.next
            lenA+=1
        while(curB.next):
            curB = curB.next
            lenB+=1
        #Step 2: If 2 last node of branch A, branch B is same (i.e: they are intersect with each other)
        
        if curA == curB:
            #Step 2.1: Compare the branch length. If branch A > branch B, then we need to advance branch A by diff
            #Where diff = lenA - lenB. Once advanced, So both A and B will start at the same place, and just try to see when they meet each other
            #That will be the intersection point
            if lenA > lenB:
                diff = lenA - lenB
                for _ in range(diff):
                    headA = headA.next
            else:
                diff = lenB - lenA
                for _ in range(diff):
                    headB = headB.next
            #Once advanced, So both A and B will start at the same place, and just try to see when they meet each other
            #That will be the intersection point
            while (headA != headB and headA and headB):
                headA = headA.next
                headB = headB.next
            return headA
                
                    
