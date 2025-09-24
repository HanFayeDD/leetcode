# Definition for singly-linked list.
from typing import Optional



class ListNode:
    def __init__(self, val=0, next=None):
        self.val:int = val
        self.next:ListNode = next
        
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fakehead = ListNode()
        fakehead.next = head
        return self.mergesort(fakehead).next
        
    def mergesort(self, head:ListNode)->ListNode:
        if head.next is None or head.next.next is None:
            return head
        
        lpart, rpart = self.sep(head)
        lpart = self.mergesort(lpart)
        rpart = self.mergesort(rpart)
        
        res = self.merge(lpart, rpart)
        
        return res 
        
    
        
    def sep(self, head: ListNode):
        lhead = ListNode()
        rhead = ListNode()
        
        quick = head
        slow = head
        
        while quick.next is not None and quick.next.next is not None:
            quick = quick.next.next
            slow = slow.next
        
        ## 长度为0 3 1  拆成 03 和 01    
        lhead = head
        rhead.next = slow.next
        slow.next = None
        
        ## 长度为0 3 拆成
        
        return lhead, rhead
    
    def merge(self, l:ListNode, r:ListNode):
        """ 
            入参：带头节点
            出参：带头节点
        """
        reshead = ListNode()
        tail = reshead
        l = l.next
        r = r.next
        
        while l is not None and r is not None:
            if l.val <= r.val:
                tail.next = l 
                l = l.next
                tail = tail.next
            else:
                tail.next = r 
                r = r.next
                tail = tail.next
        if l is not None:
            tail.next = l 
        if r is not None:
            tail.next = r 
        
        return reshead

    
        
        
if __name__ == "__main__":
    p10 = ListNode(10)
    p2 = ListNode(2)
    p1 = ListNode(1)
    p10.next = p2 
    p2.next = p1 
    res = Solution().sortList(p10)
    while res is not None:
        print(res.val)
        res = res.next
    


## empty 10 2 1
### 第一次
### empty 10  and  empty 2 1

### 第二次 em