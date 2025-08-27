from typing import List


## todo pass 但是可以优化
class Solution1:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ## dp[i]标识以nums[i-1]结尾的最大递增子序列的长度
        dp = [1] * (len(nums)+1)
        dp[0] = 0
        for i in range(1, len(dp)):
            nownumidx = i - 1
            nownumval = nums[nownumidx]

            residx = -1
            resmaxdp = -float('inf')
            ##找到小于nownumval的数 且对应的dp应该最大
            for idx in reversed(range(0, nownumidx+1)):
                if nums[idx] < nownumval and resmaxdp < dp[idx+1]:
                    residx = idx
                    resmaxdp = dp[idx+1]
            
            if residx == -1:
                continue
                
            dp[i] = dp[residx+1] + 1
        return max(dp)
    

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)

        for i in range(len(dp)):
            maxdpidx = -1
            maxdpval = -float('inf')
            for j in reversed(range(0, i+1)):
                if nums[j] < nums[i] and dp[j] > maxdpval:
                    maxdpidx = j
                    maxdpval = dp[j]
            
            if maxdpidx == -1:
                continue

            dp[i] = dp[maxdpidx] + 1

        return max(dp)
                    
            

    
if __name__=="__main__":
    print(Solution().lengthOfLIS([0]))

