from typing import List


## 如果有返回对应的idx
## 如果没有返回插入idx
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2  # 防止溢出，等同于 (left + right)//2
            
            if nums[mid] == target:       
                return mid
            elif nums[mid] < target: ## 1 3 5 7现在搜到5 left=right=2 target为6.left = mid + 1 = 3
                left = mid + 1
            else:## 1 3 5 7现在搜到5 left=right=2 target为4.left = mid = 2
                right = mid - 1
        
        # 如果没找到，返回应该插入的位置(left)
        return left

# 测试用例
if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    # print(search_insert(nums, 5))  # 输出: 2 (找到)
    
    ## left rigth mid
    ## 0    3     1         搜索0 0 
    ## 0    0     0         嗖嗖1 0 


    # print(search_insert(nums, 7))  # 输出: 4 (插入位置)
    # print(search_insert(nums, 0))  # 输出: 0 (插入位置)
