from typing import List

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        left = []
        for i in range(len(nums)):
            if i == 0:
                left.append(0)
                continue
            left.append(left[-1] + nums[i-1])
        
        right = [0] * len(nums)
        for i in reversed(range(len(nums))):
            if i == len(nums)-1:
                right[i] = 0
                continue
            right[i] = right[i+1] + nums[i+1]
           
        cnt = 0 
        for l, r, n in zip(left, right, nums):
            if n == 0 and l == r:
                cnt += 2
            if n == 0 and abs(l-r)==1:
                cnt += 1
        return cnt

if __name__=="__main__":
    print(Solution().countValidSelections([1,0,2,0,3]))
        