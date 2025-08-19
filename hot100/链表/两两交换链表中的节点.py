from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next:ListNode = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        emptyhead = ListNode()
        emptyhead.next = head
        p1 = emptyhead
        p2 = emptyhead

        while p1.next is not None and p1.next.next is not None:
            p2 = p1.next.next
            tmp = p2.next
            p2.next = p1.next
            p1.next.next = tmp
            p1.next = p2
            p1 = p1.next.next

        return emptyhead.next