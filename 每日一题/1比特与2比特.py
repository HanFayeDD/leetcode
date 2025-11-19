from typing import List

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        idx = 0
        l = len(bits)
        last = None
        while idx < l:
            if bits[idx] == 0:
                idx += 1
                last = 1
            else:
                idx += 2
                last = 2 
                
        return last == 1
    
if __name__ == "__main__":
    print(Solution().isOneBitCharacter([1, 1, 1, 0]))
        
            