


class Solution:
    def cutRope(self , n: int) -> int:
        maxres = -float('inf')

        for m in range(2, n+1):
            avgint = n // m 
            left = n % m 
            
            tmp = 1
            
            for i in range(1, m+1):
                if i <= left:
                    tmp *= (avgint+1)
                else:
                    tmp *= avgint
            
            maxres = max(tmp, maxres)
        return maxres