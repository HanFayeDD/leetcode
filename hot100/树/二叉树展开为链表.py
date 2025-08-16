# Definition for a binary tree node.]
## todo 使用O（1）的空间

## pass
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def search(node:TreeNode):
            nonlocal res 
            if not node:
                return 
            res.append(node.val)
            search(node.left)
            search(node.right)
            
        if not root:
            return None
        res = []
        search(root)
        root.left = None
        root.right = None
        tail = root 
        for num in res[1:]:
            tmpnode = TreeNode(num)
            tail.right = tmpnode
            tail = tail.right
        