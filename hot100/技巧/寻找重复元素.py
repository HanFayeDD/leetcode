from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = 1
        right = len(nums)-1

        while left <= right:
            mid = left + (right-left) // 2
            addsum = [num for num in nums if left <= num <= mid]
            if len(addsum) <= mid - left + 1:
                left = mid + 1
            else:
                right = mid - 1

        return left
    
if __name__ == "__main__":
    print(Solution().findDuplicate([3,3,3,3,3]))