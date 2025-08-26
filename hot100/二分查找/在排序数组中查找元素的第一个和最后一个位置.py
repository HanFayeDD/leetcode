from typing import List

## 判断是否找到的条件有所变化
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def isleftbound(idx):
            nonlocal nums, target
            if idx == 0 and nums[idx] == target:
                return True
            if nums[idx] == target and nums[idx-1] != target:
                return True
            return False
        def isrightbound(idx):
            nonlocal nums, target
            if idx == len(nums)-1 and nums[idx] == target:
                return True
            if nums[idx] == target and nums[idx+1] != target:
                return True
            return False
        

        left, right = 0, len(nums)-1

        leftbound = -1
        ## 找寻左边界
        while left <= right:
            mid = left + (right-left)//2
            
            if isleftbound(mid):
                leftbound = mid 
                break
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                right = mid - 1
        
        left, right = 0, len(nums)-1

        rightbound = -1
        ## 找寻右边界
        while left <= right:
            mid = left + (right-left)//2
            if isrightbound(mid):
                rightbound = mid 
                break
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                left = mid + 1

        return [leftbound, rightbound]

if __name__=="__main__":
    print(Solution().searchRange([5, 7, 7], 6))
