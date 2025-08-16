# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def search(depth, node:TreeNode):
            nonlocal res 
            if not node:
                return
            if depth > len(res):
                res.append(node.val)
            search(depth+1, node.right)
            search(depth+1, node.left)
        res = []
        search(1, root)
        return res 