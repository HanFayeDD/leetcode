from typing import List


## pass 但是时间复杂度高。近似O(n**2)
class Solution1:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * len(s)

        for i in range(len(s)):
            if s[i] == "(":
                dp[i] = 0
            else:
                right = i 
                left = right-1
                if left < 0:
                    continue

                while left >= 0 and dp[left] != 0: ## 跨过1
                    left -= 1
                
                ## 没有找到0
                if left < 0:
                    continue

                ## 找到了第一个0
                if s[left] == "(":
                    dp[left] = 1
                    dp[right] = 1
        
        maxcnt = -float('inf')
        nowcnt = 0
        for ele in dp:
            if ele == 1:
                nowcnt += 1
            else:
                maxcnt = max(maxcnt, nowcnt)
                nowcnt = 0

        maxcnt = max(maxcnt, nowcnt)
    
        return maxcnt        


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        pass
        maxlength = 0
        leftcnt = 0
        rightcnt = 0
        for ele in s:
            if ele == "(":
                leftcnt += 1
            if ele == ")":
                rightcnt += 1

            if rightcnt > leftcnt:
                maxlength = max(maxlength, 2 * leftcnt)
                leftcnt = 0
                rightcnt = 0

            if rightcnt == leftcnt:
                maxlength = max(maxlength, 2 * leftcnt)

        
        
        leftcnt = 0
        rightcnt = 0
        for ele in s[::-1]:
            if ele == "(":
                leftcnt += 1
            if ele == ")":
                rightcnt += 1
            
            if leftcnt > rightcnt:
                maxlength = max(maxlength, 2*rightcnt)
                leftcnt = 0
                rightcnt = 0 

        if rightcnt == leftcnt:
            maxlength = max(maxlength, 2 * leftcnt)
        
        return maxlength
            
            



if __name__=="__main__":
    print(Solution().longestValidParentheses("(()"))