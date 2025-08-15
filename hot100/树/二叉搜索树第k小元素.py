# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def search(node:TreeNode):
            nonlocal path
            if node is None:
                return None
            ## 提前返回
            if len(path) == k:
                return
            search(node.left)
            if len(path) == k:
                return
            path.append(node.val)
            if len(path) == k:
                return
            search(node.right)
            

        path = []
        search(root)
        return path[k-1]
