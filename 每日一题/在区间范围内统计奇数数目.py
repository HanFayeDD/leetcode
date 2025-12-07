class Solution:
    def countOdds(self, low: int, high: int) -> int:
        l = high - low + 1
         
        if l % 2 == 0:
            return l // 2
        else:
            if low % 2 != 0:
                return 1 + l // 2
            else:
                return l // 2 