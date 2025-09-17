from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(depth:int, path:List):
            nonlocal usedcol, usedxieup, usedxiedown, n, res
            if depth == n:
                res.append(path.copy())
                return
            
            row = depth + 1
            for col in range(1, n+1):
                xieupval    = self.calxieup(col, row)
                xiedownval  = self.calxiedown(col, row)
                if col not in usedcol and xieupval not in usedxieup and xiedownval not in usedxiedown:
                    path.append(col)
                    usedcol.add(col)
                    usedxieup.add(xieupval)
                    usedxiedown.add(xiedownval)
                    dfs(row, path)
                    path.pop()
                    usedcol.remove(col)
                    usedxieup.remove(xieupval)
                    usedxiedown.remove(xiedownval)        
        usedcol = set()
        usedxieup = set()
        usedxiedown = set()
        
        res = []
        path = []
        dfs(0, path)
        # print(res)
        resc = []
        for ele in res:
            tmp = []
            for idx in ele:
                s = ["."]*n 
                s[idx-1] = "Q"
                s = "".join(s)
                tmp.append(s)
            resc.append(tmp)
        print(resc)
             
        
        
        
    
    def calxieup(self, col, row):
        return row - col 

    def calxiedown(self, col, row):
        return row + col
         
if __name__=="__main__":
    print(Solution().solveNQueens(4))
        
        