from typing import List

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        ## 保存0才能保证最左边的数可以在区间里表示
        sumarr = [0]
        for i in range(len(nums)):
            if i == 0:
                sumarr.append(nums[0])
                continue
            sumarr.append(sumarr[-1] + nums[i])
            
        mins = [float('inf')] * k
        res = -float('inf')
        
        for idx, val in enumerate(sumarr):
            leftidx = idx % k ## 左区间也需要是求余值为leftidx的
            ## 当长度没有达到k时，这里需要的mins[leftidx]都为无穷大、res为无限小
            res = max(res, val - mins[leftidx])
            mins[leftidx] = min(mins[leftidx], val) ## 左区间的前缀和尽可能小
        
        return res 
    
if __name__ == "__main__":
    print(Solution().maxSubarraySum(nums = [-1, 10, -1], k = 1))
            
            