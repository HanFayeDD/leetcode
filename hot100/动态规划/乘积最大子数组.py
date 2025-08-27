from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dpmax = nums.copy()
        dpmax = [1] + dpmax

        ## dpmin[i]表示以nums[i-1]结尾的连续序列的最小值

        dpmin = nums.copy()
        dpmin = [1] + dpmin

        for i in range(1, len(dpmax)):
            dpmax[i] = max(dpmax[i-1]*nums[i-1], dpmin[i-1]*nums[i-1], dpmax[i])
            dpmin[i] = min(dpmax[i-1]*nums[i-1], dpmin[i-1]*nums[i-1], dpmin[i])
        
        return max(dpmax[1:])
    
if __name__=="__main__":
    print(Solution().maxProduct([0, 2]))
