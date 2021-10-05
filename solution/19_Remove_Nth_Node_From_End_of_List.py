class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_len, cur_node = 0, head
        while(cur_node):
            list_len+=1
            cur_node = cur_node.next
        if list_len == 1: return None
        if list_len == n: head = head.next
        else:
            i, idx, cur_node = 1, list_len - n, head
            while(i < idx):
                cur_node = cur_node.next
                i+=1
            cur_node.next = cur_node.next.next
        return head
        
