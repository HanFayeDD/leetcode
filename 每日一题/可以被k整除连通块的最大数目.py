from typing import List

# dfs即可。把满足要求的节点（其以及自身以下和能被k整除的）进行标记。从底往上进行标记。
# 再进行分割
# 比如A - B  A - C ，三个节点都满足要求。那么可以将其拆分成3个连通块。

# 比如 A - B  A - C 只有A能被k整除、B和C的和才能被k整除、各自不能被k整除
# 可以先dfs。B及其以下、C及其以下都不能被整除。A及其以下能被，所以加过加1

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        tbl = [set() for _ in range(n)]
        for line in edges:
            x, y = line[0], line[-1]
            tbl[x].add(y)
            tbl[y].add(x)
        
        ## 起始值是0，不是1.因为遍历到根节点时候一定会+1
        res = 0
        visited = set()
        
        def dfs(idx):
            nonlocal res, tbl 
            visited.add(idx)

            
            sonssum = 0 
            for nxt in tbl[idx]:
                if nxt in visited:
                    continue
                nxtval = dfs(nxt)
                if nxtval is not None:
                    sonssum += (nxtval % k)
            
            selfandbolowsum = (values[idx] + sonssum) % k 
            if selfandbolowsum == 0:
                # print(idx) 
                res += 1
                 
            return selfandbolowsum
            
        dfs(0)
        
        return res 
    
if __name__ == "__main__":
    print(Solution().maxKDivisibleComponents(n = 7, edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], values = [3,0,6,1,5,2,1], k = 3)) 