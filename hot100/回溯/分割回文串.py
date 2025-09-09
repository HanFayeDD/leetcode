from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[True]*n for _ in range(n)]
        
        for i in range(n-1, -1, -1):
            for j in range(i+1, n, 1):
                dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
                
        tmp = []
        res = []
        print(*dp, sep="\n")
        def dfs(nowidx):
            nonlocal tmp
            nonlocal res  
            ##!!!递归到终点时，记得创建副本，再添加至结果
            if nowidx > n-1:
                res.append(tmp.copy())
            
            for i in range(nowidx, n, 1):
                if dp[nowidx][i]:
                    tmp.append(s[nowidx:i+1])
                    dfs(i+1)
                    tmp.pop()
                
        dfs(0)
        return res 
        
        

if __name__=="__main__":
    s = Solution()
    print(s.partition("b"))        