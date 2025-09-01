## 注意第一行和第一列的特殊情况

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(1, n+1):
            dp[1][i] = dp[1][i-1] + grid[0][i-1] 

        for i in range(2, m+1):
            for j in range(1, n+1):
                if j == 1:
                    dp[i][j] = dp[i-1][j] + grid[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1] ) + grid[i-1][j-1]

        # print(*grid, sep="\n")
        # print(*dp, sep="\n")
        return dp[-1][-1]
    
if __name__=="__main__":
    print(Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]]))