from typing import List
from collections import defaultdict

# 经验1：尽量延后除法计算，表示斜率时可以用gcd化简
## 旧版本coef = p1[1] - ((p2[1]-p1[1]) / (p2[0]-p1[0])) * p1[0]
## 新版本b = (p1[1]*dx - p1[0]*dy) / dx
## 最完美的做法依然是上一条回答中提到的：完全不使用除法，而是使用 GCD 化简后的 (dy, dx) 元组作为斜率 Key，使用 y * dx - x * dy 的整数结果作为截距 Key。

# 经验2：数值转字符串
## 前面的符号可能一并转了
## 好的习惯是直接用数值做key
## In [1]: a = dict()

# In [2]: a[0.00] = 100

# In [3]: a[-0.00] = 1

# In [4]: print(a)
# {0.0: 1}

## 使用字符串做key可能会带来意想不到的错误
# In [5]: a = -0.00

# In [6]: s = str(a)

# In [7]: print(s)
# -0.0
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        inf = float('inf')
        kcoefd = defaultdict(int)
        kd = defaultdict(int)
        kmidd = defaultdict(int)
        midd = defaultdict(int)
        for i in range(len(points)):
            p1 = points[i]
            for j in range(i+1, len(points)):
                p2 = points[j]
                if p1[0] == p2[0]:
                    kcoefd[f'{inf}##{p1[0]}'] += 1
                    kd[f"{inf}"] += 1
                    mid = (p1[0]+p2[0], p1[1]+p2[1])
                    kmidd[f"{inf}##{mid}"] += 1
                    midd[f"{mid}"] += 1
                else:
                    dy = p1[1] - p2[1]
                    dx = p1[0] - p2[0]
                    k = dy / dx 
                    ## 除法在最后一步，误差比较小
                    b = (p1[1]*dx - p1[0]*dy) / dx 
                    xielv = k 
                
                    # xielv = (p2[1]-p1[1]) / (p2[0]-p1[0])
                    if xielv >= 0:
                        xielv = abs(xielv)
                    # coef = p1[1] - xielv*p1[0]
                    coef = b
                    if coef >= 0:
                        coef = abs(coef)
                    kcoefd[f"{xielv}##{coef}"] += 1
                    kd[f'{xielv}'] += 1
                    mid = (p1[0]+p2[0], p1[1]+p2[1])
                    kmidd[f"{xielv}##{mid}"] += 1
                    midd[f"{mid}"] += 1
        
        res = 0 
        for kandcoef in kcoefd:
            t1 = kcoefd[kandcoef]
            t2 = kd[kandcoef.split("##")[0]]
            res += t1 * (t2 - t1) 
        
        res = res // 2 ## 这里可不能写成res //= 2意思完全不一样了
        print(kd)
        print(kcoefd)
        numdiff = 0
        for k in kmidd:
            t1 = kmidd[k]
            t2 = midd[k.split('##')[-1]]
            numdiff += t1 * (t2 - t1)
            
        numdiff = numdiff // 2
        
        return res - numdiff     
        
    
    
if __name__ == "__main__":
    print(Solution().countTrapezoids([[34,88],[-62,-38],[26,88],[91,88],[47,-38]]))
                