from typing import List, Dict
import heapq

## 好像可以用并查集
class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        pass

# pass
class Solution1:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        route:Dict[int, List] = dict()
        for i in range(1, c+1):
            route[i] = []
        
        for ele in connections:
            p1, p2 = ele[0], ele[1]
            route[p1].append(p2)    
            route[p2].append(p1)
        
        def dfs(node:int):
            nonlocal visited, group, belong
            visited.add(node)
            group.append(node)
            belong[node] = group
            for n in route[node]:
                if n not in visited:
                    dfs(n)
            
        visited = set()   
        groups = [] 
        belong = dict()
        for i in range(1, c+1):
            if i in visited:
                continue
            group = []
            dfs(i)
            groups.append(group)
            
        for g in groups:
            heapq.heapify(g)
        
        res = []
        offline = set()
        for opt, node in queries:
            if opt == 1:
                if node not in offline:
                    res.append(node)
                else:
                    belongg = belong[node]
                    while len(belongg) != 0 and belongg[0] in offline:
                        heapq.heappop(belongg)
                    if len(belongg) == 0:
                        res.append(-1)
                    else:
                        res.append(belongg[0])
                
            elif opt == 2:
                offline.add(node)
            # print(groups)
        return res
            
if __name__=="__main__":
    print(Solution().processQueries(c = 5, connections = [[1,2],[2,3],[3,4],[4,5]], queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]))