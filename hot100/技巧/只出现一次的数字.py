from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = None
        for i in range(len(nums)):
            if res is None:
                res = nums[i]
            else:
                res ^= nums[i]
        return res