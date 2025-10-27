from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        cnt1ls = []
        for line in bank:
            num1 = line.count('1')
            if num1 != 0:
                cnt1ls.append(num1)
        
        cnt = 0
        for i in range(len(cnt1ls)-1):
            cnt += cnt1ls[i]*cnt1ls[i+1]
            
        return cnt
            