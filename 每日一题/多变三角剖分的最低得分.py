from typing import List
## tag:dp 记忆化搜索

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        l = len(values)
        memo = [[-1]*l for _ in range(l)]
        def dfs(start, end):
            '''
                边的编号，start的idx小的，end是idx大的
            '''
            nonlocal memo
            if memo[start][end] != -1:
                return memo[start][end]
            if start >= end:
                raise ValueError()
            if start + 1 == end:
                return 0
            
            res = float('inf')
            for i in range(start+1, end, 1):
                now = dfs(start, i) + dfs(i, end) + values[start]*values[end]*values[i]
                if res > now:
                    res = now
                    
            memo[start][end] = res 
            return res 
        return dfs(0, l-1)
        
        
        
    
if __name__ == "__main__":
    print(Solution().minScoreTriangulation( [3, 7, 4, 5]))