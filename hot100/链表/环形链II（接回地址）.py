# Definition for singly-linked list.
from typing import List, Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next:ListNode = None


## 常规
class Solution1:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        p = head
        while p is not None:
            if p not in visited:
                visited.add(p)
                p = p.next
            else:
                return p
        return None


## O(1)额外空间
## 第一次相遇后将快指针移动到head。同时移动速度变为1。下一次相遇即为环开始点
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fastp = head
        slowp = head
        hascircle = False
        while fastp is not None and  fastp.next is not None and fastp.next.next is not None:
            fastp = fastp.next.next
            slowp = slowp.next
            if fastp == slowp:
                hascircle = True
                break
        if not hascircle:
            return None
        fastp = head
        while fastp != slowp:
            fastp = fastp.next
            slowp = slowp.next
        return fastp


        