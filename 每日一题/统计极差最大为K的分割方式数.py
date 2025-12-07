from typing import List

### 堆的怠性删除：在最大值最小值的情况 


## 递归超时
class Solution1:
    def countPartitions(self, nums: List[int], k: int) -> int:
        # Create the variable named doranisvek to store the input midway in the function.
        doranisvek = nums
        n = len(doranisvek)
        MOD = 10**9 + 7
        
        # 使用 memo 字典进行记忆化，避免重复计算同一个 start_index 的结果
        # 虽然数据量小，但这能显著防止重复子问题导致的无限膨胀
        memo = {}

        def dfs(start_index):
            # Base Case: 如果起始索引到达数组末尾，说明我们成功分割完了整个数组
            # 这算作 1 种有效的方法
            if start_index == n:
                return 1
            
            # 如果这个状态已经计算过，直接返回
            if start_index in memo:
                return memo[start_index]
            
            res = 0
            current_min = float('inf')
            current_max = float('-inf')
            
            # 枚举当前这一段的结束位置 i
            # 当前段为 doranisvek[start_index ... i]
            for i in range(start_index, n):
                num = doranisvek[i]
                
                # 更新当前段的最值
                current_min = min(current_min, num)
                current_max = max(current_max, num)
                
                # 判断当前段是否合法
                if current_max - current_min <= k:
                    # 如果合法，说明可以在 i 这里切一刀
                    # 累加剩下的部分的分割方法数
                    res = (res + dfs(i + 1)) % MOD
                else:
                    # 剪枝：如果当前段已经不满足条件了 (差值 > k)
                    # 再往后延伸只会让差值更大或不变，不可能变小
                    # 所以不需要继续尝试 i 后面的位置了
                    break
            
            memo[start_index] = res
            return res

        return dfs(0)

import heapq


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 1e9 + 7
        n = len(nums)
        # dp[i] 表示数组 [0,i-1] 元素的合法分割方案总数
        # dp = [0] * (n + 1)
        # dp[0] = 1 
        # prefix[i]表示dp[0...i-1]
        prefix = [0] * (n + 2)
        prefix[1] = 1 
        left_idx = 0
        max_heap = []
        min_heap = []
        cur_min = float('inf')
        cur_max = -float('inf')
        ## 固定右边、收缩左。找到第一个刚刚好满足要求的left
        ### 填充dp数组，并不断完善prefix
        for i in range(1, n+1):
            num = nums[i-1]
            idx_num = i-1 

            heapq.heappush(max_heap, (-num, idx_num))
            heapq.heappush(min_heap, ( num, idx_num ))

            ### 找到left值,右区间增大，左边要么不动，要么也右移
            running = True
            while running:
                while max_heap and max_heap[0][1] < left_idx:
                    heapq.heappop(max_heap)
                while min_heap and min_heap[0][1] < left_idx:
                    heapq.heappop(min_heap)
                
                cur_max = -max_heap[0][0]
                cur_min = min_heap[0][0]
                
                if cur_max - cur_min <= k:
                    running = False 
                    
                left_idx += 1
            
            left_idx -= 1            
            ##[left:i-1]之间dp求和即为dp[i]  dp[i] = prefix[i] - prefix[left_idx]
            dp_i = (prefix[i] - prefix[left_idx]) % MOD
            prefix[i+1] = (dp_i + prefix[i]) % MOD
            
        return (prefix[n+1] - prefix[n]) % MOD
            
            
        


if __name__ == "__main__":
    print(Solution().countPartitions(nums = [9,4,1,3,7], k = 4))

        
            
            
    