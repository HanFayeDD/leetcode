# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val:int = val
        self.left:TreeNode = left
        self.right:TreeNode = right
        
## not pass存在问题，得到的最大的链条可能不是一条线
class Solutio1:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node:TreeNode):
            nonlocal maxsum
            if node is None:
                return 0 
            
            nowsum = node.val + dfs(node.left) + dfs(node.right)
            
            maxsum = max(nowsum, maxsum)
            
            return 0 if nowsum <= 0 else nowsum
            
            
        
        
        maxsum = -float('inf')
        dfs(root)
        return maxsum
    
    
class Solution():
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node:TreeNode):
            nonlocal maxsum
            if node is None:
                return 0 
            
            lres = dfs(node.left) 
            rres = dfs(node.right)
            
            nowsum = node.val
            
            if lres <= 0 and rres <= 0:
                pass
            elif lres <= 0 and rres > 0:
                nowsum += rres
            elif lres > 0 and rres <= 0:
                nowsum += lres
            else:
                nowsum += (lres + rres)
            
            ## 自己是拐点，更新最大值
            maxsum = max(nowsum, maxsum)
            
            ## 将自己单链的最大共享上报给父节点
            return max(node.val + lres, node.val + rres, node.val)
            
        
        maxsum = -float('inf')
        dfs(root)
        return maxsum