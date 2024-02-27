# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                tmp = cur
                while tmp and tmp.next:
                    if tmp.val == tmp.next.val:
                        tmp = tmp.next
                    else:
                        break
                cur.next = tmp.next
            cur = cur.next
        return head
