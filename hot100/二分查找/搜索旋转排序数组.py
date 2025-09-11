from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        
        leftmin = nums[0]
        rightmax = nums[-1]
        
        while left <= right:
            leftmin = nums[left]
            rightmax = nums[right]
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid 
            
            ## 区间是旋转了
            if leftmin > rightmax:
                if target >= leftmin:
                    if target < nums[mid]:
                        right = mid - 1     
                    else:
                        ## nums[mid]是否与target在同一区间
                        if nums[mid] >= leftmin:
                            left = mid + 1
                        else:
                            right = mid - 1
                elif target <= rightmax:
                    if target < nums[mid]:
                        ## 判断mid是不是与target在同一部分
                        if nums[mid] <= rightmax:
                            right = mid - 1
                        else:
                            left = mid + 1
                    else:
                        left = mid + 1  
                else:
                    return -1 

            ## 区间没有旋转
            else:
                if target > nums[mid]:
                    left = mid + 1 
                else:
                    right = mid - 1
        
        return -1
    
    
if __name__=="__main__":
    print(Solution().search([8,1,2,3], 8))
    