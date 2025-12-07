from typing import List

## pass 
class Solution1:
    def countPartitions(self, nums: List[int]) -> int:
        numsprefix = []
        sum_ = 0
        for i in range(len(nums)):
            sum_ += nums[i]
            if i == 0:
                numsprefix = [nums[i]]
            else:
                numsprefix.append(numsprefix[-1] + nums[i])
                
        res = 0 
        for i in range(0, len(nums)-1):
            l = numsprefix[i]
            r = sum_ - numsprefix[i]
            if (l - r) % 2 == 0:
                res += 1
    
        return res 

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        sum_ = sum(nums)
        prefixsum = 0
        res = 0
        for i in range(len(nums)-1):
            prefixsum += nums[i]
            right = sum_ - prefixsum 
            if (prefixsum - right) % 2 == 0:
                res += 1
        
        return res 