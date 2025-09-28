from typing import List

## i和i-1都不行，那么其他组合更不可能行
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1, 1, -1):
            if nums[i] < nums[i-1] + nums[i-2]:
                return nums[i] + nums[i-1] + nums[i-2]
        return 0