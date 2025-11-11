from typing import List

## 被弹出的是山峰（两边都有小于其的值）
## 留下来的是小的值

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = []
        cnt = 0
        for num in nums:
            if len(stack) == 0 or stack[-1] < num:
                stack.append(num)
            elif stack[-1] > num:
                while len(stack) != 0 and stack[-1] > num:
                    stack.pop()
                    cnt += 1
                if len(stack) == 0 or stack[-1] != num:
                    stack.append(num)
        
        return cnt + len(stack) - (stack[0]==0)
    
if __name__=="__main__":
    print(Solution().minOperations(nums=[3, 1, 2, 1]))