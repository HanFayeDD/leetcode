from typing import List


## 先排序、再动态规划 no pass all
class Solution1:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums  = sum(nums)
        
        if sum_nums % 2 != 0:
            return False
        
        target = sum_nums // 2

        dp = [[None]*len(nums) for _ in range(len(nums))]
        nums.sort()

        for left in range(len(nums)):
            for right in range(left, len(nums)):
                if right == left:
                    dp[left][right] = nums[left]
                    if dp[left][right] == target:
                        return True
                    continue

                dp[left][right] = dp[left][right-1] + nums[right]
                if dp[left][right] == target:
                    return True
        
        return False

## pass
class Solution2:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums  = sum(nums)
        
        if sum_nums % 2 != 0:
            return False
        
        target = sum_nums // 2

        ## dp[i]表示nums中选取数字相加，能否得到target
        dp = [False] * (target + 1)
        dp[0] = True
        

        ## 是每多考虑一个数字、就会对dp产生影响。
        ## 因此外层是每一个数字、内层是更新对dp的影响
        for num in nums:
            ## num固定的情况下，从前往后遍历dp，dp[i]变为true、dp[i+num]也会变为true。相当于num用了两次。
            ## 在一次内循环中，不改变旧dp即可
            newdp = dp.copy()

            for i in range(1, target+1):
                if i - num >= 0 and dp[i - num]:
                    newdp[i] = True

            dp = newdp
        
        # for i in range(len(dp)):
        #     print(f"{i}:{dp[i]}", end=" ")
        return dp[target]


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums  = sum(nums)
        
        if sum_nums % 2 != 0:
            return False
        
        target = sum_nums // 2

        ## dp[i]表示nums中选取数字相加，能否得到target
        dp = [False] * (target + 1)
        dp[0] = True
    
        ## 是每多考虑一个数字、就会对dp产生影响。
        ## 因此外层是每一个数字、内层是更新对dp的影响
        for num in nums:
            ## 前面的会对后面的造成影响，所以从后面往前面更新dp
            for i in range(len(dp)-1, num-1, -1):
                dp[i] = dp[i] or dp[i-num]
        
        return dp[target]

if __name__=="__main__":
    print(Solution().canPartition([1,5,11,5]))