# Definition for singly-linked list.
from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        emptyhead = ListNode()
        emptyhead.next = head
        p1 = emptyhead
        p2 = emptyhead

        cnt = 0
        while p2 is not None and cnt <n:
            p2 = p2.next
            cnt += 1
        if p2 is None:
            return head
        
        while p2.next is not None:
            p1 = p1.next
            p2 = p2.next

        lefthead = None
        if p1.next is not None and p1.next.next is not None:
            lefthead = p1.next.next 

        p1.next = lefthead

        return emptyhead.next

        
            
