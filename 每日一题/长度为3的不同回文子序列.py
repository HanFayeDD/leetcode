class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        cnt = 0
        anum = ord("a")
        znum = ord("z")
        for i in range(anum, znum+1):
            nowchar = chr(i)
            l = s.find(nowchar)
            if l < 0:
                continue
            r = s.rfind(nowchar) 
            cnt += len(set(s[l+1:r]))
            
        return cnt
        
        
    
if __name__=="__main__":
    print(Solution().countPalindromicSubsequence("aabca"))