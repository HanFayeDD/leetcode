from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next:ListNode = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        emptyhead = ListNode()
        emptyhead.next = head
        p1 = emptyhead
        p2 = None

        while True:
            p2 = p1 
            
            cnt = 0
            while p2.next is not None and cnt < k:
                p2 = p2.next
                cnt += 1
            ## 不足k个
            if cnt != k:
                break

            tmphead = p1
            p1 = tmphead.next
            ## 翻转[p1 p2]之间
            ## p1在翻转过程中已经在不断移动了
            ## 很工整 注意看左边变量和右边变量的对应关系（斜着对应）
            for i in range(k-1):
                nowmove = p1.next

                p1.next = nowmove.next

                nowmove.next = tmphead.next

                tmphead.next = nowmove
        return emptyhead.next
