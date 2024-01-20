# 3. Linked List

## 3.1. Keynotes

### `dummy_head` and `dummy_tail`

- Create a linked list with `dummy_head` and `tail`: `dummy_head = tail = ListNode(val=0, next=None)` using `tail` to move ([21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/))
- Create a `dummy_head = None` for the case do NOT require extra node.

### `tmp` to store the reference

- Some we might need to make the change to the `.next` of the `curr` node, so we can use `tmp = curr.next` to store the reference of the `curr` node before we points `curr.next` to another node

```Python
dummy_head = None

while head:
    # use tmp to store the head.next (reference of the remaining list)
    tmp = head.next
    # point head.next to dummy_head
    head.next = dummy_head
    # move dummy_head to head
    dummy_head = head
    # re-assign head back to the tmp (reference of the remaining list)
    head = tmp
```

### Fast & Slow Pointer

- **Floyd's Tortoise and Hare Algorithm**: Use 2 pointers slow fast to traverse, if slow meets fast, meaning it is a cycle linked list
  - NOTE: need to ensure both `fast` & `fast.next` is not `None` as fast pointer moved by `(fast.next).next`
- **Application**: detect if the linked list contains cycle, find the middle point of the linked list

```Python
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False

        slow, fast = head, head.next
        # need to ensure both fast & fast.next is not NULL
        # as fast pointer moved by (fast.next).next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
```
