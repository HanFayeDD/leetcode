from typing import List


## 时间复杂度、空间复杂度均为o（n）时间
class Solution1:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numset = set(nums)

        res = 1
        while True:
            if res not in numset:
                return res
            res += 1

## 时间复杂度o（n）、空间复杂度o（1）
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ## 答案在[1, len(num)+1]之间。为len(num)+1时说明所有[1, len(num)]都有了
        
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = float('inf')

        ## 用如果idx对应的值为负数，则表示idx+1这个数出现过
        ## 如果num出现了，则把num-1标记为负数
        for i in range(len(nums)):
            nownumabs = abs(nums[i])

            ## 大于len（nums）的数字不用标记
            if 1 <= nownumabs <= len(nums):
                nums[nownumabs-1] = -abs(nums[nownumabs-1])

        ## 找到第一个值为正的idx
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        
        return len(nums) + 1
            
            



