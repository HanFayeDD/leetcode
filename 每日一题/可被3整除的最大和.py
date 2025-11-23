from typing import List

## 贪心
class Solutio1:
    def maxSumDivThree(self, nums: List[int]) -> int:
        nums.sort()
        leftis1 = []
        leftis2 = []
        snums = sum(nums)
        for num in nums:
            if num % 3 == 1:
                leftis1.append(num)
            elif num % 3 == 2:
                leftis2.append(num)
        
        ans = 0
        if snums % 3 == 0:
            return snums
        elif snums % 3 == 1:
            if len(leftis1) >= 1:
                ans = snums - leftis1[0]
            if len(leftis2) >= 2:
                ans = max(ans, snums - leftis2[0] - leftis2[1])
        elif snums % 3 == 2:
            if len(leftis2) >= 1:
                ans = snums - leftis2[0]
            if len(leftis1) >= 2:
                ans = max(ans, snums - leftis1[0] - leftis1[1])
        return ans

## no pass
class Solution2:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [[0] * len(nums) for _ in range(3)]
        n = len(nums)
        for i in range(n):
            left = nums[i] % 3
            if i == 0:
                dp[0][0] = nums[0] if left == 0 else 0 
                dp[1][0] = nums[0] if left == 1 else 0
                dp[2][0] = nums[0] if left == 2 else 0
                continue
        
            ## 只有当dp[1][i]、dp[2][i]被首次更新后，此规则才起作用
            if left == 0:
                dp[0][i] = dp[0][i-1] + nums[i]
                dp[1][i] = dp[1][i-1] + nums[i] if dp[1][i-1] != 0 else dp[1][i-1]
                dp[2][1] = dp[2][i-1] + nums[i] if dp[2][i-1] != 0 else dp[2][i-1]
                
            elif left == 1:

                dp[0][i] = max(dp[0][i-1], dp[2][i-1] + nums[i]) 
                dp[1][i] = max(dp[1][i-1], dp[0][i-1] + nums[i]) 
                dp[2][i] = max(dp[2][i-1], dp[1][i-1] + nums[i])
           
                
            elif left == 2:
                dp[0][i] = max(dp[0][i-1], dp[1][i-1] + nums[i]) 
                # （2 + 2） % 3 = 1但是存在着 （0 + 2） % 3 = 2导致更新错误
                dp[1][i] = max(dp[1][i-1], dp[2][i-1] + nums[i]) 
                dp[2][i] = max(dp[2][i-1], dp[0][i-1] + nums[i])
        print(nums)
        print()
        print(*dp, sep="\n")
        return dp[0][-1]
    
## pass
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # dp[0]: 当前能得到的余数为0的最大和
        # dp[1]: 当前能得到的余数为1的最大和
        # dp[2]: 当前能得到的余数为2的最大和
        dp = [0, 0, 0]

        # 遍历数组中的每一个数字
        for num in nums:
            # 创建一个dp数组的副本，以防在单次迭代中错误地使用了本次更新后的值
            # dp_next 存储本次迭代计算出的新值
            dp_next = dp.copy()

            # 遍历上一轮计算出的三个最大和 (dp[0], dp[1], dp[2])
            for current_sum in dp:
                # 将当前数字num与之前的和相加
                new_sum = current_sum + num
                
                # 计算新和的余数
                remainder = new_sum % 3
                
                # 更新对应余数的最大和
                # 我们要取 “不加num时的最大和” 与 “加了num之后的新和” 中较大的一个
                dp_next[remainder] = max(dp_next[remainder], new_sum)
            
            # 用本轮计算出的新状态更新dp数组，为下一轮做准备
            dp = dp_next

        # 最终结果是所有数字遍历完后，余数为0的最大和
        return dp[0]                
    
if __name__ == "__main__":
    print(Solution().maxSumDivThree([1,2,3,4,4]))