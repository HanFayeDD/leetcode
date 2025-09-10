from typing import List
from queue import Queue



class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotvisited = set()
        initrot = set()
        q = Queue()
        
        m = len(grid)
        n = len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotvisited.add((i, j))
                    initrot.add((i, j))
        cnt = 0
        q.put(initrot)
        while not q.empty():
            item = q.get()
            tmpset = set()
            for ele in item:
                if ele[0]-1 >= 0 and grid[ele[0]-1][ele[1]] == 1 and (ele[0]-1, ele[1]) not in rotvisited:
                    rotvisited.add((ele[0]-1, ele[1]))
                    tmpset.add((ele[0]-1, ele[1]))
                if ele[0]+1 <= m-1 and grid[ele[0]+1][ele[1]] == 1 and (ele[0]+1, ele[1]) not in rotvisited:
                    rotvisited.add((ele[0]+1, ele[1]))
                    tmpset.add((ele[0]+1, ele[1]))
                if ele[1]-1 >= 0 and grid[ele[0]][ele[1]-1] == 1 and (ele[0], ele[1]-1) not in rotvisited:
                    rotvisited.add((ele[0], ele[1]-1))
                    tmpset.add((ele[0], ele[1]-1))
                if ele[1]+1 <= n-1 and grid[ele[0]][ele[1]+1] == 1 and (ele[0], ele[1]+1) not in rotvisited:
                    rotvisited.add((ele[0], ele[1]+1))
                    tmpset.add((ele[0], ele[1]+1))
            if len(tmpset) == 0:
                break
            q.put(tmpset)
            cnt += 1
            
            
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in rotvisited:
                    return -1
            
        return cnt  
    
    
                    
if __name__=="__main__":
    print(Solution().orangesRotting(  [[2,1,1],[0,1,1],[1,0,1]]))