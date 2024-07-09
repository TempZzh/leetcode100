from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        fakeHead = ListNode()
        fakeHead.next = head
        pre = fakeHead
        cur = head
        while cur is not None:
            while (cur.next is not None) and (cur.val == cur.next.val):
                cur = cur.next
            if pre.next == cur:
                pre = pre.next
            else:
                pre.next = cur.next
            cur = cur.next
        return fakeHead.next

def printLinked(node: Optional[ListNode]):
    if node is None:
        print('NULL')
        return
    print(node.val, end='->')
    printLinked(node.next)

def generateLinked(arr: list):
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
        
    return head

if __name__ == '__main__':
    root = generateLinked([1, 1, 1, 2, 3])
    printLinked(root)
    printLinked(Solution().deleteDuplicates(root))
