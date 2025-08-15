# Definition for a binary tree node.


## 审题错误--关于平衡二叉树

from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        midnum = nums[len(nums)//2]
        root = TreeNode(midnum)
        root.left = self.convertleft(nums[:(len(nums)//2)])
        root.right = self.convertright(nums[(len(nums)//2)+1:])
        return root
        
    def convertleft(self, ls:list):
        ls.reverse()
        head = TreeNode()
        tail = None
        for ele in ls:
            tmp = TreeNode(val=ele)
            if tail is None:
                head.left = tmp
                tail = tmp
            else:
                tail.left = tmp
                tail = tail.left
        return head.left

    def convertright(self, ls:list):
        ls.reverse()
        head = TreeNode()
        tail = None
        for ele in ls:
            tmp = TreeNode(val=ele)
            if tail is None:
                head.left = tmp
                tail = tmp
            else:
                tail.left = tmp
                tail = tail.left
        return head.left



