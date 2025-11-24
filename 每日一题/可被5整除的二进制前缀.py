from typing import List

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = [False] * len(nums)
        nownum = 0 
        for i, bit in enumerate(nums):
            nownum = (nownum << 1) | bit 
            # print(nownum)
            nownum %= 5 
            if nownum == 0:
                res[i] = True
        return res 
    
if __name__ == "__main__":
    print(Solution().prefixesDivBy5([0,1,1]))