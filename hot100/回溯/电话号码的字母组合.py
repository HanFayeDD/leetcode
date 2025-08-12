from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numtoalphasdict = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        res = []
        def dfs(depth, path):
            if depth == len(digits):
                if len(path) == 0:
                    return 
                res.append("".join(path))
                return
            
            for alpha in numtoalphasdict[digits[depth]]:
                path.append(alpha)
                dfs(depth+1, path)
                path.pop()
            
        path = []
        dfs(0, path)
        return res
    
if __name__=="__main__":
    s= Solution()
    print(s.letterCombinations(""))



