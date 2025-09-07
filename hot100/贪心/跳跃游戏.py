from typing import List
## no pass超时
class Solution1:
    def canJump(self, nums: List[int]) -> bool:
        canreach = [False]*len(nums)
        canreach[0] = True
        for idx, num in enumerate(nums):
            if idx == len(nums)-1:
                break
            
            if canreach[idx]:
                for i in range(num):
                    canreach[min(idx+i+1, len(canreach)-1)] = True
                    
        return canreach[-1]            


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxidx = 0        
        ## 判断是否在最远范围内
        ## 更新最远范围
        ## 判断最远范围超出了右边界没
        for i in range(len(nums)-1):
            if i <= maxidx:
                maxidx = max(maxidx, i + nums[i])
                if maxidx >= len(nums)-1:
                    return True
        if maxidx >= len(nums)-1:
            return True
        return False
     