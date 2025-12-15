from typing import List

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        def cal_period(l:int)->int:
            return (l+1)*l//2
                    
        res = 0
        period_l = 0 
        n = len(prices)
        for i in range(n):
            if i == 0:
                period_l += 1 
                continue 
            
            if prices[i] - prices[i-1] == -1:
                period_l += 1 
            else:
                res += cal_period(period_l)
                period_l = 1 
        
        res += cal_period(period_l)
        
        return res 
    
if __name__=="__main__":
    print(Solution().getDescentPeriods(prices = [3,2,1,4]))        
            