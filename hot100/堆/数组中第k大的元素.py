# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

# 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

# 你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。

# 1 <= k <= nums.length <= 105
# -104 <= nums[i] <= 104


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MAX = 10**4
        ls = [0]*(2*(10**4)+1)
        for num in nums:
            ls[num+MAX] += 1
        
        cnt = 0
        for num in range(2*MAX, -1, -1):
            if cnt < k and cnt+ls[num] >= k:
                return num - MAX
            cnt += ls[num]
        return -1
