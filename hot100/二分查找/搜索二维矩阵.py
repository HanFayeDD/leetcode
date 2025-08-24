from typing import List

## 展平后二分
class Solution1:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        startmn = (0, 0)
        endmn = (m-1, n-1)
        
        startidx = n*startmn[0] + startmn[1]
        endidx = n*endmn[0] + endmn[1]

        while startidx <= endidx:
            mididx = startidx + (endidx - startidx)//2
            
            if matrix[mididx//n][mididx%n] == target:
                return True
            elif matrix[mididx//n][mididx%n]  < target:
                startidx = mididx + 1
            else:
                endidx = mididx - 1
        
        return False
            

## 先找到行、再二分
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        rowidx = self.findrowidx(matrix, 0, m-1, target)

        exist = self.findoneline(matrix[rowidx], 0, n-1, target)

        return exist

    def findoneline(self, nums, start, end ,target):
        while start <= end:
            mid =  start + (end-start)//2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        
        return False
    
    def findrowidx(self, matrix, start, end, target):
        while start <= end:
            mid = start + (end-start)//2
            if matrix[mid][0] == target:
                return mid 
            elif matrix[mid][0] < target:
                start = mid + 1 
            else:
                end = mid - 1
        
        return start - 1


if __name__=="__main__":
    print(Solution().searchMatrix([[1]], 2))