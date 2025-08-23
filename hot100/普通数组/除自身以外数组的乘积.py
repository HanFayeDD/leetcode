from typing import List

## 空间复杂服为O(n)
class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [None] * len(nums)
        r = [None] * len(nums)

        l[0] = 1
        r[-1] = 1
        
        ## i)的左边累计乘
        ## (i的右边累计乘
        for idx in range(len(nums)):
            if idx == 0:
                continue
            l[idx] = l[idx-1] * nums[idx-1]

        for idx in range(len(nums)-1, -1, -1):
            if idx == len(nums)-1:
                continue

            r[idx] = r[idx+1] * nums[idx+1]

        res = []
        for i in range(len(l)):
            res.append(l[i]*r[i])

        return res
         


## 空间复杂度为O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ## l作为返回的列表
        l = [None] * len(nums)
        l[0] = 1
        for idx in range(len(nums)):
            if idx == 0:
                continue
            l[idx] = l[idx-1] * nums[idx-1]

        ## 从尾部开始向前遍历l，这样R可以积累乘积
        r = 1
        for i in reversed(range(len(nums))):
            l[i] = l[i] * r
            r = r * nums[i]
        
        return l

    