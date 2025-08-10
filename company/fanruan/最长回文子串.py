class Solution:
    def longestPalindrome(self, s: str) -> str:
        resbeginidx = 0
        resmaxlen = 1
        maxidx = len(s)-1
        for idx, val in enumerate(list(s)):
            ## 窗口3是否存在
            expand3 = True
            if idx - 1< 0 or idx+1 > maxidx:
                expand3 = False
            ### 存在进行拓展 131从131开始拓展
            if expand3 and s[idx-1] == s[idx+1]:
                left = idx 
                right = idx 
                while left>=0 and right<=maxidx and s[left] == s[right]:
                    left -= 1
                    right += 1
                if ((right-1)-(left+1)+1) > resmaxlen:
                    resbeginidx = (left+1)
                    resmaxlen = ((right-1)-(left+1)+1)

            ## 窗口4是否存在
            ### 注意这里判断条件与窗口3是否存在的类似性
            expand4 = True
            if idx < 0 or idx+1 > maxidx:
                expand4 = False
            ### 存在进行拓展 2442从44开始拓展
            if expand4 and s[idx] == s[idx+1]:
                left = idx
                right = idx+1
                while left>=0 and right<=maxidx and s[left]==s[right]:
                    left -= 1
                    right += 1
                if ((right-1)-(left+1)+1) > resmaxlen:
                    resbeginidx = (left+1)
                    resmaxlen =  ((right-1)-(left+1)+1) 

        return s[resbeginidx:resbeginidx+resmaxlen]
    



            
            
            
