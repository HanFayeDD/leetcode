from typing import List

## no pass
class Solution1:
    def rob(self, nums: List[int]) -> int:
        dp = [[0]*(len(nums)+1) for _ in range(2)] ##dp[i] i>=1表示考虑i]家能够获得的最大金额 第一行为不偷 第二行为偷
        
        for i in range(1, len(dp[0])):
            if i == 1:
                ## 不偷
                dp[0][i] = 0
                ## 偷
                dp[1][i] = nums[i-1]
                continue

            ## 不偷. 2 1 1 2没过
            dp[0][i] = max(dp[0][i-2]+nums[i-1-1], dp[1][i-1]) ## 第一个为i-2没偷、i-1偷。这里逻辑错误，也有可能i-1也不偷
            ## 偷
            dp[1][i] = dp[0][i-1]+nums[i-1] ## 第一个为i-1不偷、i偷

        return max(dp[0][-1], dp[1][-1])
    




class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [[0]*(len(nums)+1) for _ in range(2)] ##dp[i] i>=1表示考虑i]家能够获得的最大金额 第一行为不偷 第二行为偷
        
        for i in range(1, len(dp[0])):
            if i == 1:
                ## 不偷
                dp[0][i] = 0
                ## 偷
                dp[1][i] = nums[i-1]
                continue

            ## 不偷
            dp[0][i] = max(dp[0][i-1], dp[1][i-1]) ## 不偷的话，i-1可以偷也可以不偷，只要是最大的就好
            ## 偷
            dp[1][i] = dp[0][i-1]+nums[i-1]## 第一个为i-1不偷、i偷

        return max(dp[0][-1], dp[1][-1])
    
        # ===============最简单想法=============
        # dp[i][1]表示偷第i间房的最大金额，dp[i][0]表示不偷这间房的最大金额
        # 递推关系
        # ① dp[i][1] = dp[i-1][0] + nums[i] # 偷这间房 则上一次肯定不能偷
        # ② dp[i][0] = max(dp[i-1][0], dp[i-1][1]) # 不偷这间房的最大，则是上一次不管偷不偷的最大
        # ===============优化===============================
        # 若dp[i]表示直到第i间房的最大金额 
        # 首先明确dp[i][0] = dp[i-1]  因为第i个房间不偷的最大金额就等于第i-1个房间的最大金额
        # 则上面式子可以表示为
        # ① dp[i][1] = dp[i-2] + nums[i][因为dp[i-1][0] = max(dp[i-2][0],dp[i-2][1])==dp[i-2]]
        # ② dp[i][0] = dp[i-1]
        # 故dp[i] = max(dp[i][1],dp[i][0])= max(dp[i-2] + nums[i], dp[i-1])
        # 从而得到递推关系  
   
        
        
        




