from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        need_del = 0
        if len(strs) == 0 or len(strs[0]) == 0:
            return 0 
        
        def onecol(col):
            row_num = len(strs)
            min_val = -float('inf')
            for i in range(row_num):
                if ord(strs[i][col]) >= min_val:
                    min_val = ord(strs[i][col])
                else:
                    return False
            return True
        
        col_num = len(strs[0])
        
        for i in range(col_num):
            if onecol(i):
                continue
            else:
                need_del += 1
                
        return need_del
                