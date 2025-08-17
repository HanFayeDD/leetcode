# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ## 注意参数类型啊
        def search(node:TreeNode):
            nonlocal resnode
            reshasp, reshasq = False, False
            if node is None:
                return reshasp, reshasq
            
            if node.val == p.val:
                reshasp = True
            elif node.val == q.val:
                reshasq = True

            lefthasp, lefthasq = search(node.left)
            righthasp, righthasq = search(node.right)

            reshasp = reshasp or lefthasp or righthasp
            reshasq = reshasq or lefthasq or righthasq

            if reshasp and reshasq and resnode is None:
                resnode = node 

            return reshasp, reshasq

        


        resnode = None
        search(root)
        return resnode
    
if __name__=="__main__":
    p1 = TreeNode(1)
    p2 = TreeNode(2)
    p3 = TreeNode(3)
    p4 = TreeNode(4)
    p5 = TreeNode(5)
    p1.left = p2
    p1.right = p3
    p2.left = p4
    p2.right = p5
    print(Solution().lowestCommonAncestor(p1, p2, p3).val)
    
