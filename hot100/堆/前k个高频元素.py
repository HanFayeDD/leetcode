import heapq
## 小顶堆
## python中堆的使用


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        mintopheap = []
        appearcnt = dict()
        for num in nums:
            if appearcnt.get(num, None) is None:
                appearcnt[num] = 1
            else:
                appearcnt[num] += 1

        for num, count in appearcnt.items():
            if len(mintopheap) < k:
                heapq.heappush(mintopheap, (count, num))
            else:
                if count > mintopheap[0][0]:
                    heapq.heappushpop(mintopheap, (count, num))
        
        return [num for cnt, num in mintopheap]
        