# Definition for a binary tree node.
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


## 遍历所有节点、找到一个节点左子树最大深度和右子树的最大深度之和
## return的值都是当前节点相对于root的深度
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def search(depth, node:TreeNode):
            nonlocal maxdis
            ## 叶子节点
            if node is None:
                return depth-1
            
            leftmaxdepth2root = search(depth+1, node.left)

            rightmaxdepth2root = search(depth+1, node.right)
            maxdis = max(maxdis, leftmaxdepth2root+rightmaxdepth2root-2*depth)

            ## 非叶子节点
            return max(leftmaxdepth2root, rightmaxdepth2root)
        
        maxdis = 0
        search(0, root)    
        return maxdis

