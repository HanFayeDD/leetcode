from typing import List


## 转为合并区间pass
class Solution1:
    def partitionLabels(self, s: str) -> List[int]:
        leftd = dict()
        for idx, ele in enumerate(s):
            if ele not in leftd:
                leftd[ele] = idx
        
        rightd = dict()
        for i in reversed(range(len(s))):
            if s[i] not in rightd:
                rightd[s[i]] = i
                
        ls = []
        for k in leftd:
            ls.append([leftd[k], rightd[k]])
        
        ls.sort(key= lambda x : x[0])
        
        res = []
        for ele in ls:
            if len(res) == 0:
                res.append(ele)
            lastbegin = res[-1][0]
            lastend   = res[-1][1]
            
            if lastbegin <= ele[0] and ele[0] <= lastend:
                res[-1][1] = max(res[-1][1], ele[1])
            else:
                res.append(ele)
        ans = []
        for ele in res:
            ans.append(ele[1]-ele[0]+1)
        return ans
        
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastd = dict()
        for idx, ele in enumerate(s):
            lastd[ele] = idx 
            
        left, right = 0, 0
        res = []
        for idx, ele in enumerate(s):
            if lastd[ele] > right:
                right = lastd[ele]
            
            if idx == right:
                res.append(right - left + 1)
                left = right + 1
                right = left
                    
        return res 
            
        
        
        
        
if __name__ == "__main__":
    print(Solution().partitionLabels("ababcbacaf"))