from typing import List
from collections import defaultdict
## 中间分成左右，移动的时候左边变多、右边变少
## 可以一次遍历

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        ### 找2n n 2n
        res = 0 
        n = len(nums)
        MOD = 10**9 + 7
        alld = defaultdict(int)
        leftd = defaultdict(int)
        for num in nums:
            alld[num] += 1
            
        for num in nums:
            target = 2 * num 
            res += leftd[target] * (alld[target] - leftd[target] - (num == 2 * target))
            leftd[num] += 1
            
        return res % MOD
    
if __name__ == "__main__":
    print(Solution().specialTriplets([6, 3, 6]))