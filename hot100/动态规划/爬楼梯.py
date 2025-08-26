class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1) ## 注意n=2的情况，一共有两种dp=[1, 1, 2]

        dp[0] = 1

        for i in range(1, n+1):
            detal_1 = i - 1
            detal_2 = i - 2
            if detal_1 >= 0:
                dp[i] = dp[i] + dp[detal_1] 

            if detal_2 >= 0:
                dp[i] = dp[i] + dp[detal_2]  ## 由i-2 到 i-1的方法包含在dp[i-1]中了，不能重复计算
        print(dp)
        return dp[-1]

if __name__=="__main__":
    print(Solution().climbStairs(3))