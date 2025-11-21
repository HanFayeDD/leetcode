from typing import List

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda ele : (ele[0], -ele[1]))
        cnt = 2
        
        ## 尽可能的给前面的用
        left = intervals[-1][0]
        right = intervals[-1][0] + 1
        
        for i in range(len(intervals)-2, -1 , -1):
            nowl, nowr = intervals[i][0], intervals[i][1]
            
            ## 能被覆盖到
            if nowr >= right:
                continue
            elif left <= nowr < right:
                left, right = nowl, left
                cnt += 1
            elif nowr < left:
                left, right = nowl, nowl + 1
                cnt += 2
                
        return cnt
    
            
        