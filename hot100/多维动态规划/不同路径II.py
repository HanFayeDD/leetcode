from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        dp[1][1] = 1
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if i==1 and j==1:
                    continue
                gi = i-1
                gj = j-1
                ## is block
                if obstacleGrid[gi][gj] == 1:
                    dp[i][j] = 0
                    continue
                
                ## is not block
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
                
        return dp[-1][-1]

if __name__=="__main__":
    print(Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
                

                
                