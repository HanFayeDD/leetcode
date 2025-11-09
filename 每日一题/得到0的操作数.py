class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        cnt = 0
        if num1 < num2:
            num1, num2 = num2, num1
            
        while not (num1 == 0 or num2 == 0):
            num1 = num1 - num2
            if num1 < num2:
                num1, num2 = num2, num1
            cnt += 1
            
        return cnt
    
if __name__=="__main__":
    print(Solution().countOperations(num1 = 2, num2 = 3))        