from typing import List

# 一些经验
# - 二分查找ans先保存能达到的结果
# - 二分找答案，此题中找的就是最终达到的结果
# - 区间增减用diff
# - 从左至右贪心解决

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        initpower = []
        for i in range(len(stations)):
            if i <= r:
                if len(initpower) == 0:
                    initpower.append(sum(stations[:r+1]))
                else:
                    newadd = stations[i+r] if i+r < len(stations) else 0
                    initpower.append(initpower[-1]+newadd)
            else:
                newadd = 0 if i + r > len(stations) - 1 else stations[i+r]
                initpower.append(initpower[-1] + newadd - stations[i-r-1])
         
        def isok(target)->bool:
            print(f"checking {target}")
            nonlocal k, initpower, r
            newbuildcnt = 0
            nowpower = initpower[0]
            initpowerdiff = [0] * len(initpower)
            initpowerdiff[0] = initpower[0]
            for i in range(1, len(initpower)):
                initpowerdiff[i] = initpower[i] - initpower[i-1]
            
            for i in range(len(initpower)):
                if i >= 1:
                    nowpower += initpowerdiff[i]
                if nowpower >= target:
                    continue
                ## 建造
                ### 增加计数
                newbuildcnt += (target - nowpower)
                if newbuildcnt > k:
                    return False
                ### 修改diff
                if i + 2*r + 1 <= len(initpowerdiff)-1:
                    initpowerdiff[i+2*r+1] -= target - nowpower
                    
                nowpower = target
                        
            return True
            
        nowmin = min(initpower)
        left = nowmin + k // len(stations) ## 最小 
        right = nowmin + k ## 最大  
        ans = None
        while left <= right:
            mid = left + (right - left)//2
            print(f"{left}-{right}")
            ## check的是最终的结果能不能达到
            if isok(mid):
                left = mid + 1
                ans = mid 
            else:
                right = mid - 1
                
        return ans 
    
if __name__=="__main__":
    print(Solution().maxPower(stations = [4,2], r = 1, k = 1))
        
                
                
            
                
                
                
        
         
            

        
        