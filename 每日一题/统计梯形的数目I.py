from typing import List
from collections import defaultdict

## pass
class Solution1:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        def cal_tuple_num(n:int):
            return n*(n-1)//2
        MODNUM = 10**9 + 7
        
        xlinecnt = defaultdict(int)  
    
        for ele in points:
            xlinecnt[ele[1]] += 1
            
        ks = list(xlinecnt.keys())
        for k in ks:
            if xlinecnt[k] == 1:
                del xlinecnt[k]
                
        xlinepair = defaultdict()
        pairsum = 0
        for k, v in xlinecnt.items():
            n = cal_tuple_num(v)
            xlinepair[k] = n 
            pairsum += n 
            
        # res = 0
        # for k, v in xlinepair.items():
        #     res += v * (pairsum - v)
        #     res %= MODNUM
        
        # return res // 2 
        
        ## 注意除以2和求余的先后 逻辑顺序、二者不等价
        res = 0
        for k, v in xlinepair.items():
            res += v * (pairsum - v)
    
        
        return (res // 2) % MODNUM 
        
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MODNUM = 10**9 + 7 
        ycnt = dict()
        for ele in points:
            if ele[1] not in ycnt:
                ycnt[ele[1]] = 1
            else:
                ycnt[ele[1]] += 1
                
        ans = 0 
        leiji = 0
        for k, v in ycnt.items():
            pair = v * (v - 1) // 2
            ans += pair * leiji
            leiji += pair
        
        return ans % MODNUM


if __name__ == "__main__":
    print(Solution().countTrapezoids(points = [[37,39],[-19,62],[23,-48],[-61,62],[51,59]]))
        