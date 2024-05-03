# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List, Optional
from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        counter = 0
        pq = PriorityQueue()
        for node in lists:
            if node:
                pq.put((node.val, counter, node))
                counter += 1
        
        dummy = ListNode()
        tail = dummy

        while not pq.empty():
            tail.next = pq.get()[2]
            tail = tail.next
            if tail.next:
                pq.put((tail.next.val, counter, tail.next))
                counter += 1
        
        return dummy.next


if __name__ == '__main__':
    print(Solution().mergeKLists(None))
