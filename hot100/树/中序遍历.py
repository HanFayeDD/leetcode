from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def search(node:TreeNode):
            nonlocal res 
            if node is None:
                return
            search(node.left)
            res.append(node.val)
            search(node.right)

        res = []
        search(root)
        return res 
