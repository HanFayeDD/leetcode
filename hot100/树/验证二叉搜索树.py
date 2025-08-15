# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def search(node:TreeNode, lower=float('-inf'), upper=float('inf')):## 该节点以及该节点应该属于的范围
            if node is None:
                return True
            
            if not (node.val > lower and node.val < upper):
                return False
            
            if not search(node.left, lower, node.val):
                return False
            
            if not search(node.right, node.val, upper):
                return False
            
            return True
        
        return search(root)
            
                    
