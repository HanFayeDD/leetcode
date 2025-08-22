from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])

        res = [intervals[0]]

        for ele in intervals[1:]:
            beginlast = res[-1][0]
            endlast = res[-1][1]
            beginnow = ele[0]
            endnow = ele[1]
            if endlast < beginnow:
                res.append(ele)
            elif beginnow <= endlast <= endnow:
                res[-1] = [beginlast, endnow]
        
        return res
                
