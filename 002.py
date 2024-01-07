# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode()
        cur = ListNode()
        prev.next = cur
        carry = False
        while True:
            # sum = l1.val + l2.val + carry
            sum = 0
            if l1 != None:
                sum += l1.val
                l1 = l1.next
            if l2 != None:
                sum += l2.val
                l2 = l2.next
            if carry:
                sum += 1
                carry = False
            if sum >= 10:
                carry = True
            cur.val = sum % 10
            if l1 == None and l2 == None:
                break
            cur.next = ListNode()
            cur = cur.next
        if carry:
            cur.next = ListNode(val=1)
        return prev.next

if __name__ == '__main__':
    l2 = ListNode(2)
    res = Solution().addTwoNumbers(None, l2)
    print(res.val)
    print(res.next)
