from typing import List

## 也并不是找最左边一个升序的
## by bx cz 这不完了吗 


## 非升序的一定要删除
## 升序的、得看后面的情况
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        linecnt = len(strs)
        alphacnt = len(strs[0])
        
        left = [""] * linecnt
        res = 0 
        
        ## 遍历每一列
        for i in range(alphacnt):
            ## 遍历每一个单词
            going = True
            for j in range(linecnt-1):
                if left[j+1] + strs[j+1][i] < left[j] + strs[j][i]:
                    res += 1
                    # print(f"{i}-{j}")
                    going = False
                    break
            if going:  
                for idx, word in enumerate(strs):
                    left[idx] += word[i]
            # print(left)
        return res 
    
if __name__ == "__main__":
    print(Solution().minDeletionSize(["ca","bb","ac"]))
                
                
            
    
    