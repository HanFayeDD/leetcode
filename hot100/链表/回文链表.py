from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

## 时间与空间复杂度均为O(n)
class Solution1:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        res = []
        p = head
        while p:
            res.append(p.val)
            p = p.next 

        i, j = 0, len(res)-1

        ## 2 与 3最后
        while i<=j:
            if res[i] != res[j]:
                return False
            i += 1
            j -= 1
        ## 或者直接res = res[::-1]
        return True
        
## 时间复杂度O(n)
## 空间复杂度O(1)
# 方法三：快慢指针
# 思路

# 避免使用 O(n) 额外空间的方法就是改变输入。

# 我们可以将链表的后半部分反转（修改链表结构），然后将前半部分和后半部分进行比较。比较完成后我们应该将链表恢复原样。虽然不需要恢复也能通过测试用例，但是使用该函数的人通常不希望链表结构被更改。

# 该方法虽然可以将空间复杂度降到 O(1)，但是在并发环境下，该方法也有缺点。在并发环境下，函数运行时需要锁定其他线程或进程对链表的访问，因为在函数执行过程中链表会被修改。

# 算法

# 整个流程可以分为以下五个步骤：

# 找到前半部分链表的尾节点。
# 反转后半部分链表。
# 判断是否回文。
# 恢复链表。
# 返回结果。
# 执行步骤一，我们可以计算链表节点的数量，然后遍历链表找到前半部分的尾节点。

# 我们也可以使用快慢指针在一次遍历中找到：慢指针一次走一步，快指针一次走两步，快慢指针同时出发。当快指针移动到链表的末尾时，慢指针恰好到链表的中间。通过慢指针将链表分为两部分。

# 若链表有奇数个节点，则中间的节点应该看作是前半部分。



# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/palindrome-linked-list/solutions/457059/hui-wen-lian-biao-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        pass