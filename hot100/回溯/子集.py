from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def search(depth, path):    
            if depth == len(nums):
               res.append(path.copy())
               return
            
            ## 不要这个元素
            search(depth+1, path)
            ## 要这个元素
            path.append(nums[depth])
            search(depth+1, path)
            path.pop()

        depth = 0
        contain = dict()
        for num in nums:
            contain[num] = False
        res = []
        path = []
        search(depth, path)
        return res

if __name__=="__main__":
    s= Solution()
    print(s.subsets([1,2,3]))
