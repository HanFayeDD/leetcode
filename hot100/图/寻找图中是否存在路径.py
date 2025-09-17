from typing import List
from typing import Dict, List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        stack:List[int] = []
        # expanded = set()
        visited = set()
        dmap:Dict[int, List[int]] = dict()
        for ele in edges:
            if ele[0] not in dmap:
                dmap[ele[0]] = [ele[1]]
            else:
                dmap[ele[0]].append(ele[1])
                
            if ele[1] not in dmap:
                dmap[ele[1]] = [ele[0]]
            else:
                dmap[ele[1]].append(ele[0])
        
        stack.append(source)    
        visited.add(source) ## 曾经入栈过的
        while len(stack)!=0:
            top = stack.pop()
            # expanded.add(top)
            
            if top == destination:
                return True
            
            
            for neighbor in dmap.get(top, []):
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)
                else:
                    continue
                
        return False