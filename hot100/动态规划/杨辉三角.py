from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            if i == 0:
                res.append([1])
                continue

            tmp = []
            last = res[-1]
            tmp.append(1)
            for y in range(len(last)-1):
                tmp.append(last[y]+last[y+1])
            tmp.append(1)
            res.append(tmp)
        return res
