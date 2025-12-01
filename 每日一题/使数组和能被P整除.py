from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # 1. 计算总和的余数
        # 优化：直接计算 sum(nums) % p，防止数字过大（虽然Python自动处理大数，但取模更安全）
        total_mod = 0
        for x in nums:
            total_mod = (total_mod + x) % p
            
        if total_mod == 0:
            return 0
            
        # 2. 初始化哈希表
        # 键：前缀和模 p 的值
        # 值：该余数最近一次出现的索引
        # 初始化 {0: -1} 是为了处理移除的子数组从下标 0 开始的情况
        mod_map = {0: -1}
        
        current_mod = 0
        min_len = float('inf')
        n = len(nums)
        
        for i, num in enumerate(nums):
            # 更新当前前缀和的模
            current_mod = (current_mod + num) % p
            
            # 计算我们需要寻找的目标前缀和模
            # 公式推导： (current_mod - target_mod) % p = total_mod
            # 所以 target_mod = (current_mod - total_mod + p) % p
            target_mod = (current_mod - total_mod + p) % p
            
            # 3. 查找是否存在满足条件的历史前缀和
            if target_mod in mod_map:
                prev_index = mod_map[target_mod]
                ## 示例中结果为[5,2]遍历到i=1时候，total_mod=7,cur_mod = 7,此时target_mod = 0.
                ## 结果应该为1 - （-1）
                min_len = min(min_len, i - prev_index)
            
            # 4. 更新哈希表（记录当前余数的最新索引）
            mod_map[current_mod] = i
            
        # 5. 检查结果是否合法
        # 如果 min_len 还是初始值，说明没找到
        # 如果 min_len 等于数组长度 n，说明移除了整个数组，不符合题意
        return min_len if min_len < n else -1
    
if __name__ == "__main__":
    print(Solution().minSubarray(nums = [5,2,6,3], p = 9))            
        
        