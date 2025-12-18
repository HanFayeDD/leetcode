from typing import List

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        original_profit = 0 
        additional_profit = 0 
        max_add_prof = -float('inf')
        ## 第一个窗口
        for p, st in zip(prices[:k//2], strategy[:k//2]):
            original_profit += p * st 
            additional_profit += (0 - st) * p 
            
        ## 第二个窗口
        for p, st in zip(prices[k//2:k], strategy[k//2:k]):
            original_profit += p * st 
            additional_profit += (1 - st) * p
        max_add_prof = max(0, additional_profit)
        
        for i in range(k, len(prices)):
            p, st = prices[i], strategy[i]
            original_profit += p * st
            additional_profit += (1 - st) * p + (0 - 1) * prices[i - k//2] + (strategy[i - k]) * prices[i - k] 
            max_add_prof = max(max_add_prof, additional_profit)
        
        return original_profit + max(max_add_prof, 0)
        
    
        