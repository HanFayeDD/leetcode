from typing import List
import heapq

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        """_summary_

        Args:
            nums (List[int]): _description_
            k (int): _description_ subarraysize
            x (int): _description_ topk

        Returns:
            List[int]: _description_
        """
        def cal():
            nonlocal hp, x
            leiji = 0
            tmp = hp.copy()
            for i in range(min(x, len(hp))):
                ele = heapq.heappop(tmp)
                leiji += ele[0] * ele[1]
            return leiji
            
        res = []
        d = dict()
        hp = []
        init = False
        for i in range(len(nums)-k+1):
            left = i
            right = left + k - 1
            
            if not init:
                init = True
                for j in range(right + 1):
                    if nums[j] not in d:
                        ele = [-1, -nums[j]]
                        hp.append(ele)
                        d[nums[j]] = ele
                    else:
                        d[nums[j]][0] -= 1

            else:
                ## left
                d[nums[left-1]][0] += 1
                ## right
                if nums[right] not in d:
                    ele = [-1, -nums[right]]
                    hp.append(ele)
                    d[nums[right]] = ele 
                else:
                    d[nums[right]][0] -= 1
            
            heapq.heapify(hp)
            # print(hp)
            # print(d)
            res.append(cal())
            # print(res)
            
        return res
    
    
if __name__ == "__main__":
    print(Solution().findXSum(nums = [1,1,2,2,3,4,2,3], k = 6, x = 2))
                
                
                
        