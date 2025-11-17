from typing import List

## a = none 和 a = 0 在作为判断条件的时候都是假


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        pleft = None
        pright = None
        for idx, num in enumerate(nums):
            if num != 1:
                continue
            
            if pleft is None:
                pleft = idx
                continue
            
            if pright is None:
                pright = idx 
                
            if pleft is not None and pright is not None:
                if pright - pleft - 1 < k:
                    return False
                else:
                    pleft, pright = pright, None
        
        return True
            
if __name__=="__main__":
    print(Solution().kLengthApart([1,0,0,1,0,1], 2))