from typing import List

## 1 2 3
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tail_after_last_0 = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[tail_after_last_0], nums[i] = nums[i], nums[tail_after_last_0]
                tail_after_last_0 += 1
        
        print(nums)

        tail_after_last_1 = tail_after_last_0
        for i in range(tail_after_last_1, len(nums)):
            if nums[i] == 1:
                nums[tail_after_last_1], nums[i] = nums[i], nums[tail_after_last_1]
                tail_after_last_1 += 1
        print(nums)

if __name__ == "__main__":
    print(Solution().sortColors([2,0,2,1,1,0]))