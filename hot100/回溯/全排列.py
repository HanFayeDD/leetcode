from typing import List
# 通过但很垃圾,可以用一个dict来表示nousediedx
# class Solution(object):
#     res = None
#     def permute(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         Solution.res = []
#         self.circle(nums, [], list(range(len(nums))))
#         return Solution.res

#     def circle(self, nums, already, nousediedx):
#         if len(nousediedx) == 0:
#             Solution.res.append(already)

#         for idx in nousediedx:
#             tmpalready = already.copy()
#             tmpnousediedx = nousediedx.copy()
#             tmpnousediedx.remove(idx)
#             tmpalready.append(nums[idx])
#             self.circle(nums, tmpalready, tmpnousediedx)

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(depth, path):
            if depth == len(nums):
                res.append(path.copy())
                return
            
            for num, val in used.items():## 得到的是旧状态的快照
                if not val:
                    used[num] = True
                    path.append(num)
                    dfs(depth+1, path)
                    ## 因为始终用path和used表示状态，所以需要回溯
                    ## 回溯是状态变量的回溯
                    ## 如过没有修改旧状态、而是复制了旧状态并在副本上进行修改，则不需要回溯
                    used[num] = False
                    path.pop()

        used = dict()
        for num in nums:
            used[num] = False
        res = []
        path = []
        dfs(0, path)
        return res
        