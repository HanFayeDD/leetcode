from typing import List

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        xminmax = dict() ## 一个x上对应的最大和最小y值
        yminmax = dict()
        
        for b in buildings:
            x, y = b[0], b[1]
            if x not in xminmax:
                xminmax[x] = (y ,y)
            else:
                existed = xminmax[x]
                xminmax[x] = (min(existed[0], y), max(existed[1], y))
                
            if y not in yminmax:
                yminmax[y] = (x, x)
            else:
                existed = yminmax[y]
                yminmax[y] = (min(existed[0], x), max(existed[1], x))
        res = 0
        for b in buildings:
            x, y = b[0], b[1]
            yrange = xminmax[x]
            if  not (yrange[0] < y and y < yrange[1]):
                continue
                
            xrange = yminmax[y]
            if xrange[0] < x and x < xrange[1]:
                res += 1 
        
        return res 
    
if __name__ == "__main__":
    print(Solution().countCoveredBuildings(n = 3, buildings = [[1,2],[2,2],[3,2],[2,1],[2,3]]))
                        