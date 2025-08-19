# Definition for singly-linked list.
from typing import Optional

## 进阶题目
## 判断有没有环
## 环接回去到哪个idx
## 环的大小
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next:ListNode = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_p = head
        fast_p = head
        while True:
            ## 使用什么就判断什么
            if fast_p is None or fast_p.next is None:
                return False
            slow_p = slow_p.next
            fast_p = fast_p.next.next 
            if slow_p == fast_p:
                return True

