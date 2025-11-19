from typing import List

class Solution1:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        hashset = set(nums)
        while original in hashset:
            original *= 2
        return original
    
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        mask = 0 
        for num in nums:
            k, r = num // original, num % original 
            
            ## 被整除且k刚刚好是2的幂次
            if r == 0 and k & (k-1) == 0:
                mask |= k 
                
        ## 得到最低位的0
        mask = ~mask 
        bit = mask & -mask 
        return original * bit 
                
# -mask 的二进制是 ~mask + 1   
# -mask 会使得反转后最低位的1仍然为1，高位的1变为0 
# 因此 mask & -mask 得到的是最低位的1
                