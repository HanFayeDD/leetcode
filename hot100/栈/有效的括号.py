class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ele in s:
            if len(stack) == 0:
                stack.append(ele)
                continue
            if ele == ")" and stack[-1] =="(":
                stack.pop()
            elif ele =="}" and stack[-1] == "{":
                stack.pop()
            elif ele == "]" and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(ele)
        return len(stack) == 0
    
if __name__=="__main__":
    sol = Solution()
    print(sol.isValid("[][)]{}"))

    
    