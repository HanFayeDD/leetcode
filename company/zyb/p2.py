class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param root TreeNode类 树的根节点
# @return int整型
#
class Solution:
    def getDis(self , root: TreeNode) -> int:
        def dfsmaxmin(node:TreeNode, depth:int):
            nonlocal maxval, maxdepth, minval, mindepth
            if node.left is None and node.right is None:
                if node.val > maxval:
                    maxval = node.val 
                    maxdepth = depth
                if node.val < minval:
                    minval = node.val
                    mindepth = depth
                return
            
            if node.left is not None:
                dfsmaxmin(node.left, depth+1)
            if node.right is not None:
                dfsmaxmin(node.right, depth+1)
        maxval = -float('inf')
        maxdepth = 0
        minval = float('inf')
        mindepth = 0
        dfsmaxmin(root, 0)
        # print(maxval, maxdepth, minval, mindepth, sep="##")    
        fatherdepth, _ = self.getcommonfatherdepth(root, maxval, minval)
        print(maxdepth, mindepth, fatherdepth, sep="\n")
        return (maxdepth-fatherdepth) + (mindepth-fatherdepth)
        
        
    def getcommonfatherdepth(self, node:TreeNode, p, q):
        def dfs(node:TreeNode, depth, p, q)->list[bool,bool]:
            nonlocal fatherdepth
            if node.val == p:
                return True, False
            if node.val == q:
                return False, True
            
            hasp = (node.val == p)
            hasq = (node.val == q)
            
            if node.left is not None:
                leftp, leftq = dfs(node.left, depth+1, p, q)
                hasp = hasp | leftp
                hasq = hasq | leftq
            if node.right is not None:
                rightp, rightq = dfs(node.right, depth+1, p, q)
                hasp = hasp | rightp
                hasq = hasq | rightq
                
            if hasp and hasq and fatherdepth is None:
                fatherdepth = depth
                fatherval = node.val 
            
            return hasp, hasq
        fatherdepth = None
        fatherval = None
        dfs(node, 0, p, q)
        # print(f"***{fatherdepth}")
        return fatherdepth, fatherval
        
        
        
        
        
if __name__=="__main__":
    p2 = TreeNode(2)
    p1 = TreeNode(1)
    p3 = TreeNode(3)
    p4 = TreeNode(4)
    p100 = TreeNode(100)
    p2.left = p1 
    p2.right = p3
    p1.left = p4
    p3.right = p100
    print(Solution().getDis(p2))
        
        
        