from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        nowpos = 0
        cnt = 0
        while nowpos < len(nums)-1:
            leftidx = nowpos
            rightidx = nowpos + nums[nowpos]
            if rightidx >= len(nums)-1:
                return cnt + 1
            
            nextnowpos = -1
            tmpmaxreachidx = -float('inf')
            for i in range(leftidx, rightidx+1):                
                if i + nums[i] > tmpmaxreachidx:
                    nextnowpos = i 
                    tmpmaxreachidx = i + nums[i]
                    
            nowpos = nextnowpos
            cnt += 1
            
        return cnt