# 空间复杂度为o（1）
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row0_has_0 = sum([True if num==0 else False for num in matrix[0] ]) > 0
        col0_has_0 = sum([True if matrix[i][0]==0 else False for i in range(len(matrix))]) > 0

        for rownum in range(1, len(matrix)):
            for colnum in range(1, len(matrix[0])):
                if matrix[rownum][colnum] == 0:
                    matrix[rownum][0] = 0
                    matrix[0][colnum] = 0

        for rownum in range(1, len(matrix)):
            for colnum in range(1, len(matrix[0])):
                if matrix[rownum][0] == 0 or matrix[0][colnum] == 0:
                    matrix[rownum][colnum] = 0

        if row0_has_0:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        
        if col0_has_0:
            for i in range(len(matrix)):
                matrix[i][0] = 0