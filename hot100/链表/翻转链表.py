# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nowp = head
        if head is None:
            return None

        ## 使用了nextp和nowp的字段，所以得判断这俩不为空
        ## 1 2 3 变到2 1 3 时nowp在1，还可以换一次
        ## 3 2 1时，已经反转完毕
        while nowp.next is not None:
            nextp = nowp.next
            nowp.next = nextp.next 
            nextp.next = head
            head = nextp

        return head
        


