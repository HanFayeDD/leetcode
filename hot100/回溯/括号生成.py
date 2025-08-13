from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(depth, path:List, leftcnt, rightcnt):
            if leftcnt == rightcnt and rightcnt == n and len(path) == 2*n:
                res.append("".join(path))
                return
            
            ## 任意时刻左括号数目大于等于右括号即可
            if leftcnt < n and leftcnt+1 >= rightcnt:
                path.append("(")
                dfs(depth+1, path, leftcnt+1, rightcnt)
                path.pop()
            if rightcnt < n and leftcnt >= rightcnt+1:
                path.append(")")
                dfs(depth+1, path, leftcnt, rightcnt+1)
                path.pop()
        res = []
        path = []
        dfs(0, path, 0, 0)
        return res


if __name__=="__main__":
    s = Solution()
    print(s.generateParenthesis(3))


