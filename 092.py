# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        p = dummy = ListNode()
        dummy.next = head # will affect -> p.next = head
        for _ in range(left-1):
            p = p.next
        tail = p.next
        for _ in range(right-left):
            tmp = p.next
            p.next = tail.next
            tail.next = tail.next.next
            p.next.next = tmp
        return dummy.next
