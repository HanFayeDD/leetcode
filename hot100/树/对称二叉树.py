# Definition for a binary tree node.
from typing import List, Optional
from queue import Queue
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


## TODO左右指针反方向移动判断


## TODO:能否等价为中序遍历
## [1,2,2,2,null,2]
## 输出为[None, 2, None, 2, None, 1, None, 2, None, 2, None] true
## 期待为false
## 不可行
class Solution2:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        midsearchres = self.midsearch(root)

        for leftpoint in range(len(midsearchres)):
            rightpoint = len(midsearchres)-leftpoint-1
            if midsearchres[leftpoint] != midsearchres[rightpoint]:
                return False
        
        return True
        
    def midsearch(self, node:TreeNode)->List[int|None]:
        res = []

        if node.left is not None:
            res.extend(self.midsearch(node.left))
        else:
            res.append(None)

        res.append(node.val)

        if node.right is not None:
            res.extend(self.midsearch(node.right))
        else:
            res.append(None)
        return res 

        


## 可行
class Solution1:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        def search(node:TreeNode, direction:str)->List[int]:
            q = Queue()
            res = []
            q.put(node)
            while not q.empty():
                head = q.get()
                if head is None:
                    res.append(None)
                    continue
                res.append(head.val)
                if direction == "left":
                    q.put(head.left)
                    q.put(head.right)
                elif direction == "right":
                    q.put(head.right)
                    q.put(head.left)
            return res

        if (root.left is None and root.right is not None) or (root.left is not None and root.right is None):
            return False
        
        leftls = search(root.left, "left")
        rightls = search(root.right, "right")
        for a, b in zip(leftls, rightls):
            if a != b:
                return False
        return True





        
        
        
        
        