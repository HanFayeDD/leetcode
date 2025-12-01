from typing import List


## 对于mins 
## 电池大于等于 mins，一直供电一个电脑。b1个电池 供应n1个电脑（b1 = n1）
## 其他小于mins的，所有电池电量都会耗尽，会存在替换的现象。b2个电池 供应n2个电脑
## n * x <= sum(min(b, x) for b in batteries):
## 对于第二部分的电池，电池电量都小于mins，由上面不等式可以得到 n2*mins <= 小于mins的电池电量之和 
## 所以小于mins的电池个数 b2 ＞ n2，此时能够有一个充电方案

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def isok(mins:int)->bool:
            nonlocal sum_batteries, batteries
            if mins*n <= sum([min(mins, b) for b in batteries]):
                return True
            else:
                return False
        
        res = None
        left = 0
        sum_batteries = sum(batteries)
        right = sum_batteries//n 
        while left <= right:
            mid = left + (right - left) // 2
            if isok(mid):
                res = mid 
                left = mid + 1
            else:
                right = mid - 1
        return res 
    
    
