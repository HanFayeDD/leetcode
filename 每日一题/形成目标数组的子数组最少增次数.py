from typing import List

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        diff = [target[0]]
        for i in range(1, len(target)):
            diff.append(target[i]-target[i-1])
        # print(diff )
        cnt = 0
        for ele in diff:
            if ele >= 0:
                cnt += ele 
        
        return cnt
            
            
if __name__=="__main__":
    print(Solution().minNumberOperations([1,2,3,2,1]))