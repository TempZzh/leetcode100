from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        root1, root2 = ListNode(), ListNode()
        p1, p2 = root1, root2
        while head is not None:
            if head.val < x:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next
            head = head.next
        p2.next = None
        p1.next = root2.next
        return root1.next


if __name__ == '__main__':
    printLinked(Solution().partition(generateLinked([1,4,3,2,5,2]), 3))
