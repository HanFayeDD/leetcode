from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_idx = dict()
        for idx, val in enumerate(nums):
            another = target - val
            if another in val_idx:
                return [idx, val_idx[another]]
            val_idx[val] = idx
        return []