from typing import List


## 连续注意相邻这一个条件
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsset = set(nums)
        maxlength = 0
        for num in numsset:
            if num-1 in numsset:
                continue
            
            currentmaxlength = 0
            while num in numsset:
                currentmaxlength += 1
                num += 1

            maxlength = max(maxlength, currentmaxlength)

        return maxlength

            

