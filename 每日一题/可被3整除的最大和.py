from typing import List

## 贪心
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        nums.sort()
        leftis1 = []
        leftis2 = []
        snums = sum(nums)
        for num in nums:
            if num % 3 == 1:
                leftis1.append(num)
            elif num % 3 == 2:
                leftis2.append(num)
        
        ans = 0
        if snums % 3 == 0:
            return snums
        elif snums % 3 == 1:
            if len(leftis1) >= 1:
                ans = snums - leftis1[0]
            if len(leftis2) >= 2:
                ans = max(ans, snums - leftis2[0] - leftis2[1])
        elif snums % 3 == 2:
            if len(leftis2) >= 1:
                ans = snums - leftis2[0]
            if len(leftis1) >= 2:
                ans = max(ans, snums - leftis1[0] - leftis1[1])
        return ans
        
    
if __name__ == "__main__":
    print(Solution().maxSumDivThree([3,6,5,1,8]))