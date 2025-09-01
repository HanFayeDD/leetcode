from typing import List

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, n+1):
            dp[1][i] = 1

        for i in range(2, m+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        
        return dp[-1][-1]
    
if __name__=="__main__":
    print(Solution().uniquePaths(2,2))