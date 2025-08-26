from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 问题的答案是通过子问题的最优解得到的(可能不止一个子问题)
        dp = [float('inf')] * (amount + 1)
        
        dp[0] = 0
        for i in range(1, len(dp)):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i-c]+1)
        
        if dp[-1] == float('inf'):
            return -1
        else:
            return dp[-1]