from typing import List

## 内存炸
class Solution1():
    def reversePairs(self, record: List[int]) -> int:
        maxleft = [None]*len(record)
        for idx, ele in enumerate(record):
            if idx == 0:
                maxleft[idx] = record[idx]
                continue
            maxleft[idx] = max(maxleft[idx-1], record[idx])
        res = []
        # print(maxleft)
        for right in range(1, len(record), 1):
            if record[right] >= maxleft[right-1]:
                continue 
            for left in range(0, right, 1):
                if record[left] > record[right]:
                    res.append((record[left], record[right]))
        # print(res)
        return len(res)
    
    
    
## 使用归并排序思想


class Solution:
    def reversePairs(self, record: List[int]) -> int:
        def mergesort(nums:List[int])->List[int]:
            nonlocal cnt
            if len(nums) <= 1:
                return nums
            
            mid = len(nums)//2 
            
            lres = mergesort(nums[:mid])
            rres = mergesort(nums[mid:])
            
            combine = []
            i = 0 
            j = 0
            while i < len(lres) and j < len(rres):
                if lres[i] < rres[j]:
                    combine.append(lres[i])
                    i += 1
                elif lres[i] > rres[j]:
                    # 这是因为如果 lres[i] 大于 rres[j]，那么 lres[i] 之后的所有元素都会大于 rres[j]，因此应该将这些元素都计入逆序对中。
                    combine.append(rres[j])
                    cnt += (len(lres)-1 - i + 1)
                    j += 1
                else:
                    combine.append(lres[i])
                    i += 1
                    
            if i < len(lres):
                while i < len(lres):
                    combine.append(lres[i])
                    i += 1
                    
            if j < len(rres):
                while j < len(rres):
                    combine.append(rres[j])
                    j += 1
            
            return combine    

        cnt = 0
        res = mergesort(record)
        # print(res )
        return cnt
        
    
    

        
if __name__=="__main__":
    print(Solution().reversePairs([1,3,2,3,1]))     