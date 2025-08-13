from typing import List

#用一个字典，不进行状态的回溯
#status = dict()
#  for num in candidates:
#     status[num] = 0

## 会有重复元素
# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         def dfs(path, pathsum):
#             if pathsum == target:
#                 res.append(path.copy())
#                 return

#             for _, val in enumerate(candidates):
#                 if pathsum + val > target:
#                     return
#                 path.append(val)
#                 pathsum += val
#                 dfs(path, pathsum) ## 不要在传参里做运算是个好习惯
#                 path.pop()
#                 pathsum -= val
            
#         ## 先升序
#         candidates.sort()
#         res = []
#         path = []
#         dfs(path=path, pathsum=0)
#         return res
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(depth, path, pathsum):
            if pathsum == target:
                res.append(path.copy())
                return

        
            for i in range(depth, len(candidates)):
                if pathsum + candidates[i] > target:
                    return
                path.append(candidates[i])
                dfs(i, path, pathsum+candidates[i]) ## 传入i可以重复选、传入i+1不可以重复选
                path.pop()
            
        ## 先升序
        candidates.sort()
        res = []
        path = []
        depth = 0
        dfs(depth, path=path, pathsum=0)
        return res

if __name__=="__main__":
    s = Solution()
    print(s.combinationSum([2, 3, 6, 7], 7))



  