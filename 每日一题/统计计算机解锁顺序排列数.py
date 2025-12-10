from typing import List

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 10**9 + 7
        leichen = 1
        n = len(complexity)
        for i in range(1, n):
            if complexity[i] <= complexity[0]:
                return 0
            else:
                leichen = (leichen * i) % MOD
                
        return leichen