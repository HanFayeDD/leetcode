from typing import List
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 带有冷却期的最大收益
# @param prices int整型一维数组 价格数组:prices =[x,y,z] ，每个元素代表每天的价格；
# @param k int整型 冷却天数
# @return int整型
#
class Solution:
    def maxProfit(self , prices: List[int], k: int) -> int:
        # write code here
        buyprice = float('inf')
        allprofit = 0 
        nowprofit = 0
        for i in range(len(prices)):
            if prices[i] <= buyprice:
                buyprice = prices[i]
                allprofit += nowprofit
                nowprofit = 0
            else:
                nowprofit = max(nowprofit, prices[i]-buyprice)
        print(allprofit)


if __name__=="__main__":
    print(Solution().maxProfit([1, 3, 5, 2, 6, 4],1))
                
                
        