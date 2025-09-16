from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left)//2
            rightmax = nums[right]
            
            if nums[mid] < rightmax:
                right = mid
            elif nums[mid] > rightmax:
                left = mid + 1
        return nums[left]

if __name__=="__main__":
    print(Solution().findMin([4, 1])) 
                