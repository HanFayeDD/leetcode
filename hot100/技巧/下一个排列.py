from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = len(nums)-1
        right = len(nums)-1

        left = left - 1
        while left >= 0 and nums[left] >= nums[left+1]:
            left -= 1
        
        ismax = False

        if left == -1:
            ismax = True

        if not ismax:
            while nums[right] <= nums[left]:
                right -= 1

        nums[left], nums[right] = nums[right], nums[left]

        left += 1
        right = len(nums)-1

        while left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
        # print(nums)

if __name__=="__main__":
    print(Solution().nextPermutation([4, 5, 2, 6, 3, 1]))

        
        