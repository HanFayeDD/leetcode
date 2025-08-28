from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nownum = None
        nowcnt = 0

        for i in range(len(nums)):
            if i == 0:
                nowcnt += 1
                nownum = nums[i]
                continue
            if nownum == nums[i]:
                nowcnt += 1
            else:
                nowcnt -= 1
                if nowcnt <= 0:
                    nownum = nums[i]
                    nowcnt = 1
        return nownum
        
if __name__=="__main__":
    print(Solution().majorityElement([3, 2, 3]))