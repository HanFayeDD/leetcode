from typing import List


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[[0]*k for _ in range(n)] for _ in range(m)]
        MODNUM = 10**9 + 7 
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[0][0][grid[i][j] % k] = 1 
                    continue
                for modnum in range(k):
                    if i > 0 and j > 0: 
                        lastcnt = dp[i][j-1][modnum] + dp[i-1][j][modnum]
                    elif i == 0:
                        lastcnt = dp[i][j-1][modnum]
                    elif j == 0:
                        lastcnt = dp[i-1][j][modnum]
                    target = (modnum + grid[i][j]) % k 
                    dp[i][j][target] = lastcnt % MODNUM
        # print(dp)
        return dp[-1][-1][0] % MODNUM
    
    
if __name__ == "__main__":
    print(Solution().numberOfPaths(grid = [[0,0]], k = 5))
