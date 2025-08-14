from typing import List, Optional
from queue import Queue
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        def search(node:TreeNode):
            nonlocal q,  res
            q.put(node)
            while not q.empty():
                ceng = []
                node = []
                qsize = q.qsize()
                for _ in range(qsize):
                    first = q.get()
                    node.append(first)
                    ceng.append(first.val)
                
                for ele in node:
                    if ele.left is not None:
                        q.put(ele.left)
                    if ele.right is not None:
                        q.put(ele.right)
                res.append(ceng)
            


        res = []
        q:Queue[TreeNode|str] = Queue()
        search(root)
        return res 
    
if __name__=="__main__":
    p1 = TreeNode(val=1)
    p2 = TreeNode(val=2)
    p3 = TreeNode(val=3)
    p1.left = p2
    # p1.right = p3
    print(Solution().levelOrder(p1))