

class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)

        dp = [[False]*l for _ in range(l)]

        for i in range(l):
            dp[i][i] = True

        for i in range(l-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                        