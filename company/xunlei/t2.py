from typing import List
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param nums int整型一维数组 
# @param k int整型 
# @return int整型一维数组
#
from typing import List
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param nums int整型一维数组 
# @param k int整型 
# @return int整型一维数组
#
class Solution:
    def find_palindrome_subarrays(self , nums: List[int], k: int) -> List[int]:
        # if k == 0:
        #     return []
        # write code here
        if k == 1 or k == 0:
            return list(range(len(nums)))
        if len(nums) == 0:
            return []
        
        isord = k % 2 != 0
        flag = [False]*len(nums)
        
        if isord:
            for i in range(1, len(nums)-1):
                if str(nums[i-1]) == str(nums[i+1])[::-1]:
                    flag[i] = True        
        else:
            for i in range(0, len(nums)-1):
                if str(nums[i]) == str(nums[i+1])[::-1]:
                    flag[i] = True
        
        res = []
        if isord:
            res = self.extendresord(nums, k, flag)
        else:
            res = self.extendresordnot(nums, k, flag)
        return res
                        
    def extendresord(self, nums:List[int], k:int, flag:List[bool]):
        r = []
        for i in range(len(flag)):
            if flag[i]:
                left = i-1
                right = i+1
                nowk = 1
                while left >= 0 and right <= len(nums)-1 and str(nums[left]) == str(nums[right])[::-1] and nowk < k:
                    nowk += 2
                    left -= 1
                    right += 1
                if nowk >= k:
                    r.append(i-nowk//2)
        return r 
    
    def extendresordnot(self, nums:List[int], k:int, flag:List[bool]):
        r = []
        for i in range(len(flag)):
            if flag[i]:
                left = i
                right = i+1
                nowk = 0
                while left >= 0 and right <= len(nums)-1 and str(nums[left]) == str(nums[right])[::-1] and nowk < k:
                    nowk += 2
                    left -= 1
                    right += 1
                if nowk >= k:
                    r.append(i - (k//2) + 1)
        return r 
    
if __name__=="__main__":
    print(Solution().find_palindrome_subarrays([12, 3, 21, 12, 3, 21], 3))