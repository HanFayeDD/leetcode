from typing import List

## not pass
class Solution:
    
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        
        # if nums[left] < nums[right]:
        #     return nums[left]
        
        while left <= right:
            mid = left + (right - left)//2 
            
            leftval = nums[left]
            rightval = nums[right]
            
            # if self.istarget(nums, mid, left, right):
            #     return nums[mid]
            
            ## 是否有旋转
            # if leftval <= rightval:
            #     return leftval
                    
            # else: ## 有旋转
            if leftval <= nums[mid]: ## mid在较大区域内
                left = mid + 1
                
            else:  ## mid在较小区域
                right = mid 
                
        return leftval                
                
                                


if __name__=="__main__":
    print(Solution().findMin([3, 1, 2]))