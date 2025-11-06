from typing import Counter, List, Dict
import heapq

from sortedcontainers import SortedList

class Healper():
    def __init__(self, x):
        self.large = [] ##小顶 顶部是出现次数最少的、数字最小的。[+, +]  cnt，val
        self.small = [] ##大顶 顶部是出现次数最多的、数字最大的。[-, -]
        self.xsum = 0 ## 只看修改了large的部分
        self.largelen = x 
        self.d:Dict[int, List] = dict()
    
    def insert(self, val):
        ## large和small均可能修改
        if val in self.d:
            ele = self.d[val]
            ### 修改small
            if ele[1] < 0:
                ele[0] -= 1
            ### 修改large
            else:
                self.xsum += val
                ele[0] += 1
        
        else:
            ### 修改 large
            if len(self.large) < self.largelen:
                ele = [1, val]
                self.d[val] = ele 
                self.xsum += val 
                self.large.append(ele)
            ### 修改small
            else:
                ele = [-1, -val]
                self.d[val] = ele
                self.small.append(ele)
        self.check_swap()
            
    def delete(self, val):
        if val in self.d:
            ele = self.d[val]
            if ele[1] < 0:
                ele[0] += 1
            else:
                self.xsum -= val 
                ele[0] -= 1
            self.check_swap()
        
        else:
            raise ValueError("in delete")
            
    def check_swap(self):
        if len(self.large) <= self.largelen and len(self.small) == 0:
            return
        
        change = False
        heapq.heapify(self.large)
        heapq.heapify(self.small)
        
        minlarge = self.large[0]
        maxsmall = self.small[0]
        
        ## 判断条件清楚
        if (abs(minlarge[0]) < abs(maxsmall[0])) or (abs(minlarge[0]) == abs(maxsmall[0]) and abs(minlarge[1]) < abs(maxsmall[1])):
            change = True
            minlarge = heapq.heappop(self.large)
            maxsmall = heapq.heappop(self.small)
            ## 存在出现次数为0，不影响
            self.xsum = self.xsum - minlarge[0]*minlarge[1] + maxsmall[0]*maxsmall[1]
            ### 注释掉的有问题。字典的对应关系丢失了
            # minlarge[0], minlarge[1], maxsmall[0], maxsmall[1] = -maxsmall[0], -maxsmall[1], -minlarge[0], -minlarge[1] 
            ### 正确的做法
            minlarge[0], minlarge[1] = -minlarge[0], -minlarge[1]
            maxsmall[0], maxsmall[1] = -maxsmall[0], -maxsmall[1]
            
            self.large.append(maxsmall)
            self.small.append(minlarge)
            
        if change:
            heapq.heapify(self.large)
            heapq.heapify(self.small)
        
## 超时
class Solution1:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:        
        helper = Healper(x)
        res = []
        for i in range(len(nums)):
            if i <= k-1:
                helper.insert(nums[i])
            if i == k-1:
                res.append(helper.xsum)
                continue
            
            if i > k-1:
                helper.insert(nums[i])
                helper.delete(nums[i-k])
                res.append(helper.xsum)
        return res 
    
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def add(v: int):
            if cnt[v] == 0:
                return
            p = (cnt[v], v)
            if l and p > l[0]:
                nonlocal s
                s += p[0] * p[1]
                l.add(p)
            else:
                r.add(p)

        def remove(v: int):
            if cnt[v] == 0:
                return
            p = (cnt[v], v)
            if p in l:
                nonlocal s
                s -= p[0] * p[1]
                l.remove(p)
            else:
                r.remove(p)

        l = SortedList()
        r = SortedList()
        cnt = Counter()
        s = 0
        n = len(nums)
        ans = [0] * (n - k + 1)
        for i, v in enumerate(nums):
            remove(v)
            cnt[v] += 1
            add(v)
            j = i - k + 1
            if j < 0:
                continue
            while r and len(l) < x:
                p = r.pop()
                l.add(p)
                s += p[0] * p[1]
            while len(l) > x:
                p = l.pop(0)
                s -= p[0] * p[1]
                r.add(p)
            ans[j] = s

            remove(nums[j])
            cnt[nums[j]] -= 1
            add(nums[j])
        return ans

# 作者：ylb
# 链接：https://leetcode.cn/problems/find-x-sum-of-all-k-long-subarrays-ii/solutions/3823741/python3javac-yi-ti-yi-jie-ha-xi-biao-you-3a77/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    
if __name__=="__main__":
    print(Solution().findXSum(nums = [1,1,2,2,3,4,2,3], k = 6, x = 2))
            
        
        
    
    
    
    
                
        
        
        
    
