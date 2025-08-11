## "3[a2[c]]"
## "accaccacc"

class Solution:
    def decodeString(self, s: str) -> str:
        stack:list[str] = []
        ls:list[str] = list(s)
        for ele in ls:
            ## 入
            if ele.isdigit() or ele.isalpha() or ele == "[":
                stack.append(ele)
                continue
            ## 处理"]"
            if ele == "]":
                stack.append(ele)
                repeatstring, repeattimes, poptimes = self.__find(stack)
                stack = stack[:-poptimes]
                stack.extend(repeattimes*repeatstring)
        return "".join(stack)

    def __find(self, ls:list[str]):
        leftkuohaoidx = None
        rightkuohaoidx = None
        repeatstring = ""
        repeattimes = ""
        poptimes = 0
        ## 左右括号
        for idx in range(len(ls)-1, -1, -1):
            nowchar = ls[idx]
            if nowchar == "]":
                rightkuohaoidx = idx
            if nowchar == "[":
                leftkuohaoidx = idx
            if leftkuohaoidx is not None and rightkuohaoidx is not None:
                break
        repeatstring = ls[leftkuohaoidx+1:rightkuohaoidx]
        for idx in range(leftkuohaoidx-1, -1, -1):
            nowchar = ls[idx]
            if nowchar.isdigit():
                repeattimes = nowchar + repeattimes
            else:
                break
        poptimes = 2+len(repeatstring)+len(repeattimes)
        repeattimes = int(repeattimes)
        return repeatstring, repeattimes, poptimes
        
        

if __name__=="__main__":
    sol = Solution()
    print(sol.decodeString("3[a2[c]]"))


            