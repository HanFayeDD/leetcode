
## 贪心：每次移动最左边能移动的
## 1 0part1 1 0part2
## 先移动左边的1，相当于跳过了0part1。
## 这个1与后面的1都得跳过 0part2


class Solution:
    def maxOperations(self, s: str) -> int:
        zerosep = 0
        movecnt = 0
        for i in reversed(range(len(s))):
            if i == len(s)-1:
                if s[i] == "0":
                    zerosep += 1
                    movecnt = 0
                else:
                    zerosep = 0
                    movecnt = 0
                continue
            if s[i] == "0":
                if s[i+1] == "0":
                    pass
                else:
                    zerosep += 1
            else:
                movecnt += zerosep
                
        return movecnt
    
if __name__=="__main__":
    print(Solution().maxOperations("000111"))
                