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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        head.next = self.deleteDuplicates(head.next)
        return head.next if head.val == head.next.val else head


if __name__ == '__main__':
    printLinked(Solution().deleteDuplicates(generateLinked([1, 1, 2])))
