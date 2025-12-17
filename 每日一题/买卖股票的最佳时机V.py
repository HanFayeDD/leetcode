from typing import List

EMPTY = 0
HASONE = 1
ZUOKONG = 2


class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        dp = [[[0] * 3 for _ in range(k + 1)] for _ in range(n)]
        ## dp[i][j][k] i同prices的idx(表示idx对应的结束)、j同预算交易次数、k同状态
        for i in range(1, k + 1):
            dp[0][i][HASONE] = -prices[0]
            dp[0][i][ZUOKONG] = prices[0]
        ##后一天的状态与前一天有关
        for i in range(1, n):
            for j in range(1, k + 1):
                ## 当天结束不持有股票
                ## 从EMPTY到剩下两个才是j-1
                dp[i][j][0] = max(
                    dp[i - 1][j][EMPTY],
                    dp[i - 1][j][HASONE] + prices[i],
                    dp[i - 1][j][ZUOKONG] - prices[i],
                )

                ## 当天结束有一张股票
                dp[i][j][1] = max(
                    dp[i - 1][j][HASONE], dp[i - 1][j - 1][EMPTY] - prices[i]
                )

                ## 当天结束处于做空
                dp[i][j][2] = max(
                    dp[i - 1][j][ZUOKONG], dp[i - 1][j - 1][EMPTY] + prices[i]
                )

        return dp[n - 1][k][0]
