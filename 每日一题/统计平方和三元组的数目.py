class Solution:
    def countTriples(self, n: int) -> int:
        res = 0 
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                target = i**2 + j**2
                origin = target**0.5
                if origin % 1 == 0 and origin <= n:
                    res += 2
        return res 
                    


## 暴力解法
class Solution1:
    def countTriples(self, n: int) -> int:
        square = set()
        for i in range(1, n+1):
            square.add(i**2)
        
        res = 0
        for i in range(1, n+1):
            for j in range(i+1, n+1):
               if i**2 + j**2 in square:
                   res += 2
        return res  
            
        
## 
