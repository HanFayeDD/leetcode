from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for ele in operations:
            if "+" in ele:
                x += 1
            else:
                x -= 1
                
        return x 
    
    
if __name__=="__main__":
    print(Solution().finalValueAfterOperations(["--X","X++","X++"]))