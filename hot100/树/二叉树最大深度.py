from typing import Optional, List
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def search(depth:int, node:TreeNode):
            nonlocal maxdepth
            if node.left is None and node.right is None:
                maxdepth = max(maxdepth, depth)
                return

            if node.left is not None:
                search(depth+1, node.left)
            if node.right is not None:
                search(depth+1, node.right)
        
        ## 空树
        if root is None:
            return 0

        maxdepth = 0
        search(1, root)
        return maxdepth