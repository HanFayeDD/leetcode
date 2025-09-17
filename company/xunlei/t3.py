#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param s string字符串 待匹配字符串
# @param p string字符串 模式
# @return bool布尔型
#
class Solution:
    def isMatch(self , s: str, p: str) -> bool:
        # write code here
        if len(s) == 0:
            return True
        if len(p) == 0:
            return False
        
        if p == ".*":
            return True
        
        l1 = len(s)-1
        l2 = len(p)-1
        
        p1, p2 = 0, 0
        while p1 <= l1:
            pass
        
        
        
        
        if p1 == len(s):
            return True
        else:
            return False

    
