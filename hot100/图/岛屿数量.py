from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(posi, posj):
            nonlocal visited, m, n 
                        
            if posi < 0 or posi > m-1:
                return
            if posj < 0 or posj > n-1:
                return
            if visited[posi][posj]:
                return
            visited[posi][posj] = True
            if grid[posi][posj] == "0":
                return 

            
            dfs(posi-1, posj)
            dfs(posi+1, posj)
            dfs(posi, posj-1)
            dfs(posi, posj+1)
            

        m = len(grid)
        n = len(grid[0])
        
        visited = [[False]*n for _ in range(m)]
        
        cnt = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j]=="1":
                    cnt += 1
                    dfs(i, j)
        return cnt
                    