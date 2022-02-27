from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse(head)

    def reverse(self, current: Optional[ListNode], previous: Optional[ListNode] = None):
        if not current:
            return previous

        nxt = current.next
        current.next = previous
        return self.reverse(nxt, current)
