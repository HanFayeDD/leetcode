from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        resemptyhead = ListNode()
        tail = resemptyhead
        p1 = list1
        p2 = list2

        while p1 is not None and p2 is not None:
            if p1.val <= p2.val:
                tail.next = p1 
                p1 = p1.next
                tail = tail.next
            else:
                tail.next = p2
                p2 = p2.next
                tail = tail.next
        
        if p1 is not None:
            tail.next = p1
        if p2 is not None:
            tail.next = p2

        return resemptyhead.next
                