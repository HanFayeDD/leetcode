from typing import List


## 甚至可以只用原来的grid就行
## 不需要set
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        def search(x, y, direction):
            nonlocal visited, grid
            if x < 0 or x > m-1 or y < 0 or y > n-1:
                return
            if grid[x][y] != EMPTY:
                return
            if (x,y, direction) in visited:
                return
            visited.add((x, y, direction))
            visitednode.add((x, y))
            if direction == UP:
                search(x-1, y, UP)
            elif direction == DOWN:
                search(x+1, y, DOWN)
            elif direction == LEFT:
                search(x, y-1, LEFT)
            elif direction == RIGHT:
                search(x, y+1, RIGHT)
        visited = set()
        visitednode = set()
        EMPTY = 0
        WALL = -1
        GUARD = 1
        UP = 2 
        DOWN = 3
        LEFT = 4
        RIGHT = 5
        grid = [[EMPTY]*n for _ in range(m)]
        for ele in guards:
            grid[ele[0]][ele[1]] = GUARD
            
        for ele in walls:
            grid[ele[0]][ele[1]] = WALL
            
        ## 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == GUARD:
                    search(i, j-1, LEFT)
                    search(i, j+1, RIGHT)
                    search(i-1, j, UP)
                    search(i+1, j, DOWN)
   
        
        
        return m * n - len(guards) - len(walls) - len(visitednode)
        
        
        
        
if __name__=="__main__":
    print(Solution().countUnguarded(m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]))