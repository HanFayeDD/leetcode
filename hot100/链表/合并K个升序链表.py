from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        while len(lists) != 1:
            res = []
            cnt = len(lists)//2
            for i in range(cnt):
                res.append(self.mergetwo(lists[2*i], lists[2*i+1]))
            if len(lists)%2 != 0:
                res.append(lists[-1])
            lists = res

        return lists[0]

    def mergetwo(self, la:Optional[ListNode], lb:Optional[ListNode]):
        emptyhead = ListNode()
        tail = emptyhead

        while la is not None and lb is not None:
            if la.val <= lb.val:
                tail.next = la
                la = la.next
            else:
                tail.next = lb 
                lb = lb.next
            tail = tail.next
        
        if la is not None:
            tail.next = la
        if lb is not None:
            tail.next = lb 
        
        return emptyhead.next