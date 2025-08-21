from typing import List

## no pass超时
class Solution1:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ## 开始到 idx]的累加和
        sumbeforeidx = [0]
        for _, val in enumerate(nums):
                sumbeforeidx.append(sumbeforeidx[-1]+val)
        # print(sumbeforeidx)
        cnt = 0
        for i in range(0, len(sumbeforeidx)-1):
            for j in range(i+1, len(sumbeforeidx)):
                if sumbeforeidx[j] - sumbeforeidx[i] == k:
                    cnt += 1
        return cnt
## 暴力枚举 超时
class Solution2:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ## 以i开始的
        cnt = 0
        for i in range(0, len(nums)):
            ssum = nums[i]
            if ssum == k:
                cnt += 1
            if i == len(nums)-1:
                break
            for j in range(i+1, len(nums)):
                ssum += nums[j]
                if ssum == k:
                    cnt += 1
        return cnt
    

# 前缀和 + 哈希表优化
# pre[i]标识[0,i]的和
# pre[i]−pre[j−1]==k标识[j, i]和为k
# pre[j−1]==pre[i]−k
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ## 前缀和
        presum = []
        for idx, val in enumerate(nums):
            if idx == 0:
                presum.append(val)
            else:
                presum.append(presum[-1]+val)

        appear_cnt_dict = dict()
        res = 0
        print(presum)
        ## 正对1 -1 0这种特殊的情况 1 0 0 到第一个0时，target为0，此时应该+1
        appear_cnt_dict[0] = 1 
        ## 右边的i
        for ele in presum:
            target = ele - k
            res += appear_cnt_dict.get(target, 0)
            if ele not in appear_cnt_dict:
                appear_cnt_dict[ele] = 1
            else:
                appear_cnt_dict[ele] += 1
        return res




if __name__=="__main__":
    print(Solution().subarraySum([1,-1, 0], 0))

        