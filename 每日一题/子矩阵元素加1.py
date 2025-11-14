from typing import List

## time exceed
class Solution1:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat = [[0]*n for i in range(n)]
        for line in queries:
            bh, blie, eh, elie = line[0], line[1], line[2], line[3]
            for i in range(bh, eh+1):
                for j in range(blie, elie+1):
                    mat[i][j] += 1
                    
        return mat
    
## error
class Solution2:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        matdiff = [[0]*n for i in range(n)]
        for line in queries:
            bh, blie, eh, elie = line[0], line[1], line[2], line[3]
            ## 左侧
            ### 非第一列， 需要通过水平关系找到对应的值
            if blie != 0:
                for i in range(bh, eh+1):
                    matdiff[i][blie] += 1
            ### 第一列本来竖直方向就是diff，只需修改一个
            else:
                matdiff[bh][blie] += 1
            ## 右侧所有
            if elie + 1 < n:
                for i in range(bh, eh+1):
                    matdiff[i][elie+1] -= 1
            ## 最后一行下面
            if eh + 1 < n:
                matdiff[eh+1][blie] -= 1
            print(matdiff)
        
        for i in range(n):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if j == 0:
                    matdiff[i][j] = matdiff[i-1][j] + matdiff[i][j]
                    continue
                matdiff[i][j] = matdiff[i][j-1] + matdiff[i][j]
        return matdiff      

## 每一行当作1维来解决 pass
class SolutionPass:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        matdiff = [[0]*n for i in range(n)]
        for line in queries:
            bh, bl, eh, el = line[0], line[1], line[2], line[3]
            for i in range(bh, eh+1):
                matdiff[i][bl] += 1
            
            if el+1 < n:
                for i in range(bh, eh+1):
                    matdiff[i][el+1] -= 1
            
        for i in range(n):
            for j in range(n):
                if j == 0:
                    continue
                matdiff[i][j] += matdiff[i][j-1]
        return matdiff

## 二维差分
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        matdiff = [[0]*n for i in range(n)]
        for line in queries:
            bh, bl, eh, el = line[0], line[1], line[2], line[3]
            matdiff[bh][bl] += 1
            if el + 1 < n:
                matdiff[bh][el+1] -= 1
            if eh + 1 < n:
                matdiff[eh+1][bl] -= 1
            if el + 1 < n and eh + 1 < n:
                matdiff[eh+1][el+1] += 1
        
        ## 将diff沿着行方向拓展开
        for i in range(n):
            for j in range(1, n):
                matdiff[i][j] += matdiff[i][j-1]
        
        ## 将diff沿列方向拓展开
        for i in range(1, n):
            for j in range(n):
                matdiff[i][j] += matdiff[i-1][j]
        
        return matdiff    
    
    
if __name__=="__main__":
    print(Solution().rangeAddQueries(n = 3, queries = [[1,1,2,2],[0,0,1,1]]))
        