## 边向前走，边更新最小价格作为买入价格。同时，往后迭代计算售出的利润

## 在第五天卖出的股票、一定是在前1234天最小值买入时能得到最大利润

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buyprice = float('inf')
        maxprofit = 0
        for p in prices:
            if buyprice > p:
                buyprice = p
            elif p - buyprice > maxprofit:
                maxprofit = p - buyprice
        return maxprofit

        