from typing import List
from collections import defaultdict

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        def dfs(p:int):
            nonlocal knowed, visited, g    
            knowed.add(p)
            visited.add(p)
            for n in g.get(p, []):
                if n not in visited:
                    dfs(n)
        
        meetings.sort(key= lambda x:x[2])
        
        knowed = set()
        knowed.add(0)
        knowed.add(firstPerson)
        n = len(meetings)
        i = 0
        while i < n:
            g = dict()
            t = meetings[i][2]
            while i < n and meetings[i][2] == t :
                x, y = meetings[i][0], meetings[i][1]
                if x not in g:
                    g[x] = []
                if y not in g:
                    g[y] = []
                g[x].append(y)
                g[y].append(x)
                i += 1
            
            visited = set()
            print(g)
            for k in g:
                ## 起点是没有知道秘密的、且没有遍历的
                if k in knowed and k not in visited:
                    dfs(k)
                
        return list(knowed)
    
if __name__ == "__main__":
    print(Solution().findAllPeople(n = 6, meetings =[[1,2,5],[2,3,8],[1,5,10]], firstPerson = 1))