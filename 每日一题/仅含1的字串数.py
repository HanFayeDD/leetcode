MODNUM = 1e9 + 7

class Solution:
    
    def numSub(self, s: str) -> int:
        def calsum(cnt:int):
            # nonlocal cache
            # if cnt in cache:
            #     return cache[cnt]
            
            # logic of cal
            return (cnt**2+cnt)//2
            
            
        
        # cache = dict()
        res = 0
        period = 0
        for i in range(len(s)):
            if i == 0:
                period += (s[i]=='1')
                continue
            if s[i] == '1':
                period += 1
            else:
                res += calsum(period)
                res %= MODNUM
                period = 0
        if period != 0:
            res += calsum(period)
            res %= MODNUM
        
        return int(res) 

if __name__=="__main__":
    print(Solution().numSub("0110111"))