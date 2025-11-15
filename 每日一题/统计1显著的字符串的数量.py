## 01问题注意前缀和
## 二层遍历时，可以看看有没有什么优化跳转



class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        prefix = [0]*n 
        nxt0 = [None]*n 
        for i in range(n):
            if i == 0:
                if s[i] == "0":
                    prefix[i] = 0
                else:
                    prefix[i] = 1
                continue
            if s[i] == "0":
                prefix[i] = prefix[i-1]
            else:
                prefix[i] += (prefix[i-1] + 1)

        nowzeroidx = n
        for i in reversed(range(n)):
            ## 本身是0的话也得是下一个0的位置
            nxt0[i] = nowzeroidx
            if s[i] == "0":
                nowzeroidx = i 
                
              

        res = 0
        for i in range(n):
            j = i 
            while j < n:
                cnt1 = prefix[j] - prefix[i] + (s[i] == "1")     
                cnt0 = j - i + 1 - cnt1
                if cnt1 >= cnt0**2:
                    ## 必是以1结尾
                    nj = nxt0[j]
                    res += (nj -j)
                    j = nj 
                else:
                    j += cnt0**2 - cnt1
        
        return res 
                
                
                
        
if __name__ == "__main__":
    print(Solution().numberOfSubstrings("101101"))
                        
        