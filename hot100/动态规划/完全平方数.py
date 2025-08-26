class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        for i in range(1, n+1):
            dishu = 1
            while i - dishu**2 >= 0:
                dp[i] = min(dp[i], dp[i-dishu**2]+1)
                dishu += 1
        
        print(dp)
        return dp[-1]
        
if __name__=="__main__":
    print(Solution().numSquares(12))