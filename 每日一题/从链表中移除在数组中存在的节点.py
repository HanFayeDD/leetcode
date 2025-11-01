from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next:ListNode = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        having = set(nums)
        empty = ListNode()
        empty.next = head
        p1 = empty
        p2 = empty.next
        while p2 is not None:
            if p2.val in having:
                p1.next = p2.next
                p2 = p1.next
            else:
                p1 = p1.next
                p2 = p1.next
        return empty.next
                    
            
            
                
        