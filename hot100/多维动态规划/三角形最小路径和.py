from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = []
        for i in range(n):
            dp.append([None]*(i+1))
            
        dp[0][0] = triangle[0][0]
        
        for i in range(1, n):
            numinrow = i + 1
            for j in range(numinrow):
                if j == 0:
                    dp[i][j] = dp[i-1][0] + triangle[i][j]
                elif j == numinrow-1:
                    dp[i][j] = dp[i-1][-1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
                    
        return min(dp[-1])
    
if __name__=="__main__":
    print(Solution().minimumTotal( [[2],[3,4],[6,5,7],[4,1,8,3]]))