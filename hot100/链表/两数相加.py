from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next:ListNode = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        jinwei = 0
        o1 = 0
        o2 = 0
        resemptyhead = ListNode()
        tail = resemptyhead
        while l1 is not None and l2 is not None:
            o1 = l1.val
            o2 = l2.val
            tail.next = ListNode((o1+o2+jinwei)%10)
            jinwei = (o1+o2+jinwei)//10
            tail = tail.next
            l1 = l1.next
            l2 = l2.next
        
        if l1 is not None:
            while l1 is not None:
                tail.next = ListNode(((l1.val+jinwei)%10))
                jinwei = (l1.val+jinwei)//10
                tail = tail.next
                l1 = l1.next

        if l2 is not None:
            while l2 is not None:
                tail.next = ListNode(((l2.val+jinwei)%10))
                jinwei = (l2.val+jinwei)//10
                tail = tail.next
                l2 = l2.next
        
        ## 进位处理
        if jinwei != 0:
            tail.next = ListNode(jinwei)
        
        return resemptyhead.next
        



        