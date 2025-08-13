from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        maxrow = len(board)-1
        maxcol = len(board[0])-1
        def dfs(path:List):
            if len(path) == len(word):
                return True
            comparewordidx = len(path)
            ## !!记得声明本地变量
            row = path[-1][0]
            col = path[-1][1]
            ## up
            if row-1>=0 and board[row-1][col] == word[comparewordidx] and (row-1, col) not in path:
                path.append((row-1, col))
                res = dfs(path)
                if res:
                    return res
                path.pop()
            ## down
            if row+1<= maxrow and board[row+1][col] == word[comparewordidx] and (row+1, col) not in path:
                path.append((row+1, col))
                res = dfs(path)
                if res:
                    return res
                path.pop()
            ## left
            if col-1>=0 and board[row][col-1] == word[comparewordidx] and (row, col-1) not in path:
                path.append((row, col-1))
                res = dfs(path)
                if res:
                    return res
                path.pop()
            ## right
            if col+1<=maxcol and board[row][col+1] == word[comparewordidx] and (row, col+1) not in path:
                path.append((row, col+1))
                res = dfs(path)
                if res:
                    return res
                path.pop()

            return False
        
        flag = False
        path = None
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    path = []
                    path.append((row, col))
                    flag = dfs(path)
                    if flag:
                        return flag
                    
        return flag
        

if __name__=="__main__":
    s = Solution()
    print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))        