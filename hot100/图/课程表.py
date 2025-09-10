from typing import List


## TODO：pass待优化
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(node:int):
            nonlocal flag
            ## 0 not dfs
            ## -1 no problem node就当前而言，不在环上
            ## 1 在当前搜索路径上
            if flag[node] == 1:
                return False
            if flag[node] == -1:
                return True
            
            flag[node] = 1
            
            for i in range(numCourses):
                if not dp[node][i]:
                    continue
                if not dfs(i):
                    return False
            
            flag[node] = -1
            return True
            
                
        dp = [[False]*numCourses for _ in range(numCourses)]
        for ele in prerequisites:
            dp[ele[1]][ele[0]] = True
        
        flag = [0]*numCourses
        
        for i in range(numCourses):
            if not dfs(i):
                return False
            
        return True
    
if __name__ == "__main__":
    print(Solution().canFinish(2, [[0, 1], [1, 0]]))