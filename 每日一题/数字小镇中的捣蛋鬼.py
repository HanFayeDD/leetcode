from typing import List

# 数字小镇 Digitville 中，存在一个数字列表 nums，其中包含从 0 到 n - 1 的整数。每个数字本应 只出现一次，然而，有 两个 顽皮的数字额外多出现了一次，使得列表变得比正常情况下更长。

# 为了恢复 Digitville 的和平，作为小镇中的名侦探，请你找出这两个顽皮的数字。

# 返回一个长度为 2 的数组，包含这两个数字（顺序任意）。
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        maxnum = len(nums) - 3
        orderxor = 0
        numsxor = 0
        for ele in range(maxnum+1):
            orderxor ^= ele 
        for ele in nums:
            numsxor ^= ele 
            
        resxor = orderxor ^ numsxor
        print(resxor)
        wei = 0
        for idx, ele in enumerate(list(reversed(bin(resxor)))):
            if ele == "1":
                wei = idx 
                break
        
        flag = 2**wei
        print(flag)
        
        orderxorx = 0
        orderxory = 0
        for ele in range(maxnum+1):
            if flag & ele == flag:
                orderxorx ^= ele
            else:
                orderxory ^= ele
        
        numsxorx = 0
        numsxory = 0
        for ele in nums:
            if flag & ele == flag:
                numsxorx ^= ele
            else:
                numsxory ^= ele
            
        return [orderxorx ^ numsxorx, orderxory ^ numsxory]
            
        
    
    
if __name__=="__main__":
    print(Solution().getSneakyNumbers([0,3,2,1,3,2]))