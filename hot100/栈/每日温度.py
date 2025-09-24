from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while len(stack)>0 and stack[-1][1] < temperatures[i]:
                idx, val = stack.pop()
                res[idx] = i - idx 
                
            stack.append((i, temperatures[i]))
                
        return res 
    
if __name__=="__main__":
    print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))
    
    