class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head

        dummy_head = ListNode()
        dummy_head.next = head
        
        cur, prev = head, dummy_head
        i = 1
        while(cur and i <= left-1):
            prev = cur
            cur = cur.next
            i+=1
        
        while(cur and i < right):
            temp = cur.next
            cur.next = temp.next
            temp.next = prev.next
            prev.next = temp
            i+=1

        return dummy_head.next
