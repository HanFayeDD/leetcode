# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next:ListNode = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        emptyhead = ListNode()
        emptyhead.next = head
        curemptyhead = emptyhead
        flag = True

        while flag:            
            ## 翻转currenthead和curtail之间的 -1 1 2 3 to -1 2 1 3 to -1 3 2 1
            curtail = curemptyhead
            for i in range(k):
                curtail = curtail.next
                if curtail is None:
                    flag = False
                    break

            if flag == False:
                continue
            first = curemptyhead.next
            for i in range(k-1): 
                first_after_first = first.next
                first.next = first_after_first.next
                first_after_first.next = curemptyhead.next
                curemptyhead.next = first_after_first

            curemptyhead = first

        return emptyhead.next

