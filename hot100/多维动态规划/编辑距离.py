from typing import List


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[None]*(n+1) for i in range(m+1)]

        dp[0][0] = 0
        for i in range(1, n+1):
            dp[0][i] = i

        for i in range(1, m+1):
            dp[i][0] = i

        for i in range(1, m+1):
            for j in range(1, n+1):
                idx1 = i-1
                idx2 = j-1
                if word1[idx1] == word2[idx2]:
                    dp[i][j] = dp[i-1][j-1]
                else:##分别表示删A从[i][j]变到[i-1][j]、删B、以及替换A（B）
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        
        return dp[-1][-1]