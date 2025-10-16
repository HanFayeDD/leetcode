from typing import List

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        numsyu = [ele % value for ele in nums]
        cnt = [0] * (value)
 
        for ele in numsyu:
            cnt[ele] += 1
        print(numsyu)
        print(cnt)
        ## findmin 最左边的最小值
        minidx = 0
        minval = float('inf')
        for i in range(len(cnt)):
            if cnt[i] < minval:
                minval = cnt[i]
                minidx = i 
                
        return value * minval + (minidx)
        
        
if __name__=="__main__":
    print(Solution().findSmallestInteger([1,-10,7,13,6,8], 5))