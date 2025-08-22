from typing import List
import heapq


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = dict()
        
        wnd_dict = dict()
        resstr = ""
        resstrlen = float('inf')
        for ele in t:
            if ele not in t_dict:
                t_dict[ele] = 1
                wnd_dict[ele] = 0
            else:
                t_dict[ele] += 1

        left, right = 0, 0
        while right < len(s):
            ## 加入右边
            if s[right] in wnd_dict:
                wnd_dict[s[right]] += 1
            
            ## 检查是否匹配
            if not self.matched(t_dict, wnd_dict):
                right += 1
                continue

            
            ## 缩短左边 [left, right]匹配
            while self.matched(t_dict, wnd_dict):
                if right - left + 1 < resstrlen:
                    resstr = s[left:right+1]
                    resstrlen = len(resstr)
                if s[left] in wnd_dict:
                    wnd_dict[s[left]] -= 1
                left += 1


            ## A00BOAB 窗口缩短为00B之后右边应该要+1，要不然B会重复计算
            right += 1

            
        return resstr
         
    def matched(self, d1, d2):
        for key in d1:
            if d1[key] > d2[key]:
                return False
        return True
    
if __name__=="__main__":
    print(Solution().minWindow(s = "ADOBECODEBANC", t = "ABC"))