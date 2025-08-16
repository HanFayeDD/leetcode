# Definition for a binary tree node.
from typing import List, Optional

## todo 优化 前缀和


## pass 时间太长但是
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def search(node:TreeNode):
            nonlocal path, cnt, targetSum
            if not node:
                return
            
            path.append(node.val)
            cnt += self.countsum(targetSum, path)
            search(node.left)
            search(node.right)
            path.pop()
            

        path = []
        cnt = 0
        search(root)
        return cnt

    def countsum(self, targetSum:int, path:List[int])->int:
        cnt = 0
        for i in range(1, len(path)+1):
            if sum(path[-i:]) == targetSum:
                cnt += 1
        return cnt
        
if __name__=="__main__":
    p1 = TreeNode(1)
    p2 = TreeNode(2)
    p3 = TreeNode(3)
    p1.left = p2 
    p1.right = p3
    print(Solution().pathSum(p1, 3))

      