from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """_summary_
        Args:
            strs (List[str]): _description_
            m (int): _description_ 0
            n (int): _description_ 1
        Returns:
            int: _description_
        """
        ## 对应限制下 i个1和j个0能达到的最大子集个数
        dp = [[0]*(m+1) for _ in range(n+1)] ## 第一维度是1 第二维度是0
        for s in strs:
            cnt0, cnt1 = 0, 0
            cnt0 = s.count("0")
            cnt1 = len(s) - cnt0
            for idx1 in range(n, cnt1-1, -1):
                for idx0 in range(m, cnt0-1, -1):
                    dp[idx1][idx0] = max(dp[idx1][idx0], dp[idx1-cnt1][idx0-cnt0]+1)
                    
        return dp[n][m]
            

        
        
    
if __name__ == "__main__":
    print(Solution().findMaxForm(strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3))