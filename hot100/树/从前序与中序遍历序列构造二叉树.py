# Definition for a binary tree node.
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(preo:List, ino:List)->TreeNode:
            nonlocal preoidx 
            ## 最后ino肯定越来越小、当ino长度为2的时候进入函数。会被分成长度为1和0的两部分。
            if len(ino)==1:
                preoidx += 1
                return TreeNode(val=ino[0])
            if len(ino)==0:
                return
            nownode = TreeNode(val=preorder[preoidx])
            inoidx = ino.index(preorder[preoidx])
            preoidx += 1
            nownode.left = build(preo, ino[:inoidx])
            nownode.right = build(preo, ino[inoidx+1:])
            return nownode

        if len(preorder)==1 and preorder[0]==-1 and len(inorder)==1 and inorder[0]==-1:
            return TreeNode(-1)
        preoidx = 0
        return build(preorder, inorder)

        