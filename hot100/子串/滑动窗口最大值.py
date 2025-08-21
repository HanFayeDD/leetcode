from typing import List
import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        hp = [(-nums[i], i) for i in range(k)]

        heapq.heapify(hp)
        res = [-hp[0][0]]
        for i in range(k, len(nums)):

            ## i-k已不在窗口内
            ## 3 3 1 2 
            ## 移动到3 1 2时，顶部是第一个3：删除得到3 1，再加入2，得到 3 2 1
            ## 移动到3 1 2时，顶部是第二个3:没有删除任何，还是3 3 1，再加入2，得到3 3 2 1。但是下一次两个3无论如何都会被删除
            while len(hp)!=0 and hp[0][1] <= i-k :
                heapq.heappop(hp)
            heapq.heappush(hp, (-nums[i], i))
            res.append(-hp[0][0])
        return res


print(Solution().maxSlidingWindow([1, -1], 1))


