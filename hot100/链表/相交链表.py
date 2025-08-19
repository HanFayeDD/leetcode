# Definition for singly-linked list.
from typing import List, Optional

## TODO 双指针
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited = set()
        pointa = headA
        while pointa is not None:
            visited.add(pointa)
            pointa = pointa.next
        
        pointb = headB
        while pointb is not None:
            if pointb in visited:
                return pointb
            pointb = pointb.next
        return None
