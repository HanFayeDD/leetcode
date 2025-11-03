from typing import List

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        def moveright(left):
            nonlocal colors, neededTime, MININF
            right = left
            max_ = MININF
            leiji_ = 0
            while right < len(colors) and colors[left] == colors[right]:
                leiji_ += neededTime[right]
                max_ = max(max_, neededTime[right])
                right += 1
            return right-1, leiji_, max_
                
            
            
        MININF = -float('inf')
        periodmax = MININF
        periodleiji = 0
        left, right = 0, 0
        cnt = 0
        while left < len(colors):
            right, periodleiji, periodmax = moveright(left)
            cnt += (periodleiji - periodmax)
            left = right + 1
        
        return cnt
    
if __name__=="__main__":
    print(Solution().minCost(colors = "aabaa", neededTime = [1,2,3,4,1])) 