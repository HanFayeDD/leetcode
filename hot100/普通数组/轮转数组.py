from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(ls, left, right):
            while left <= right:
                ls[left], ls[right] = ls[right], ls[left]
                left += 1
                right -= 1

        k = k % len(nums)
        reverse(nums, 0, len(nums)-1-k)
        reverse(nums, len(nums)-1-k+1, len(nums)-1)
        reverse(nums, 0, len(nums)-1)
        