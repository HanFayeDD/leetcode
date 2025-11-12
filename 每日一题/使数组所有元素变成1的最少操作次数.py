from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def gcd(a, b):
            if a < b:
                a, b = b, a 
            while b != 0:
                a, b = b, a%b 
            return a 
        n = len(nums)
        has1 = 0
        numsgcd = 0 
        for num in nums:
            if num == 1:
                has1 += 1
            numsgcd = gcd(numsgcd, num)
            
        if has1:
            return n - has1
        if numsgcd > 1:
            return -1 

        minlength = float('inf')
        for i in range(n):
            gcdperiod = nums[i]
            for j in range(i+1, n):
                gcdperiod = gcd(gcdperiod, nums[j])
                if gcdperiod == 1:
                    minlength = min(minlength, j - i + 1)
                    
        return minlength - 1 + n - 1 
        
    